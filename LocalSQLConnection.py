import sqlite3
from sqlite3 import Error

 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
 
    return conn

 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    
    query1 = """
WITH fac_mem AS (SELECT full_name,
       name AS facility
FROM Bookings AS b
LEFT JOIN Facilities AS f
ON b.facid = f.facid
LEFT JOIN (SELECT surname || ' ' || firstname as full_name,
                  memid
           FROM Members
           )AS m
ON b.memid = m.memid
WHERE b.memid != 0
GROUP BY  full_name, name)

SELECT full_name,
       GROUP_CONCAT(facility) AS facs_by_member
FROM fac_mem;"""
    cur.execute(query1)
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)


def main():
    database = "sqlite_db_pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn: 
        print("2. Query all tasks")
        select_all_tasks(conn)
 
 
if __name__ == '__main__':
    main()