import sqlite3
import os


def main():
    database_name = 'db.sqlite'
    connection = _setup_db(database_name)
    _insert_data(connection, 'input1.txt', 'input2.txt')
    _output_sorted_data(connection, 'output.txt')
    _cleanup_db(database_name, connection)


def _setup_db(database_name):
    drop_people_table = "DROP TABLE IF EXISTS people"
    create_people_table = """
    CREATE TABLE people (
        id integer PRIMARY KEY,
        first_name text,
        last_name text)
    """
    connection = sqlite3.connect(database_name)

    cursor = connection.cursor()

    cursor.execute(drop_people_table)
    cursor.execute(create_people_table)

    return connection


def _insert_data(connection, first_names_file, last_names_file):
    add_first_name_statement = """
        insert into people(id, first_name)
        values (?, ?)
    """
    add_last_name_statement = """
        update people set last_name = ? where id = ?
    """
    cursor = connection.cursor()
    first_names_file_path = _get_absolute_file_path(first_names_file)
    last_names_file_path = _get_absolute_file_path(last_names_file)

    with open(first_names_file_path) as f:
        for entry in f:
            first_name, id = entry.split()
            cursor.execute(add_first_name_statement, (id, first_name))

    with open(last_names_file_path) as f:
        for entry in f:
            last_name, id = entry.split()
            cursor.execute(add_last_name_statement, (last_name, id))


def _output_sorted_data(connection, output_file_name):
    cursor = connection.cursor()
    output_file_path = _get_absolute_file_path(output_file_name)
    select_ordered_results_statement = """
    select id, first_name, last_name
    from people order by id
    """

    with open(output_file_path, "w") as f:
        for row in cursor.execute(select_ordered_results_statement):
            id, first_name, last_name = row
            entry = "{0} {1} {2}".format(first_name, last_name, id)
            f.write("{0}\n".format(entry))


def _cleanup_db(database_name, connection):
    cursor = connection.cursor()
    connection.commit()
    connection.close()
    os.remove(database_name)


def _get_absolute_file_path(file_name):
    script_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(script_path, file_name)


if __name__ == '__main__':
    main()
