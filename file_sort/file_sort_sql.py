import sqlite3
import os

def main():
    db = './db.sqlite'
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    drop_people_table = """
    DROP TABLE IF EXISTS people
    """

    cursor.execute(drop_people_table)

    create_people_table = """
    CREATE TABLE IF NOT EXISTS people (
         id integer PRIMARY KEY,
         first_name text,
         last_name text)"""

    cursor.execute(create_people_table)

    with open('file1.txt') as f:
        for entry in f:
            first_name, id = entry.split()
            cursor.execute("insert into people(id, first_name) values (?, ?)", (id, first_name))
            
    with open('file2.txt') as f:
        for entry in f:
            last_name, id = entry.split()
            cursor.execute("insert or replace into people(id, last_name, first_name) values (?, ?, (select first_name from people where id = ?))", (id, last_name, id))

    cursor.execute("select id, first_name, last_name from people order by id")
    with open("file_output.txt", "w") as f:
        for id, first_name, last_name in cursor.fetchall():
            entry = "{0} {1} {2}".format(first_name, last_name, id)
            f.write("{0}\n".format(entry))

    cursor.execute(drop_people_table)
    conn.commit()
    conn.close()
    os.remove(db)


if __name__ == '__main__':
    main()