import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)

    except Error as e:
        print(e)


def add_account(conn, account):
    sql = '''INSERT INTO accounts(email,username,encoded_pass)
            VALUES(?,?,?)
    '''

    cur = conn.cursor()
    cur.execute(sql, account)
    conn.commit()
    return cur.lastrowid


def add_tasks(conn, task):
    sql = '''INSERT INTO tasks(title,description,begin_date,end_date)
            VALUES(?,?,?,?)
    '''

    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def create_task(conn, name, description, begin_time, end_time):
    with conn:
        task = (name, description, begin_time, end_time)
        add_tasks(conn, task)


def create_accounts(conn, username, email, coded_pass):
    with conn:
        account = (username, email, coded_pass)
        add_account(conn, account)


def accounts_db(db):
    database = db

    sql_create_accounts_table = ''' CREATE TABLE IF NOT EXISTS accounts (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        email text NOT NULL,
                                        encoded_pass text NOT NULL
                                    ); '''

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_accounts_table)
    else:
        print("Error! cannot create the database connection.")


def tasks_db():
    database = r"C:\Users\Dell\Desktop\File folder\Python\Agileroo\To Do App\database\tasks.db"

    sql_create_accounts_table = ''' CREATE TABLE IF NOT EXISTS tasks (
                                            id integer PRIMARY KEY,
                                            title text NOT NULL,
                                            description text NOT NULL,
                                            begin_date text NOT NULL,
                                            end_date text NOT NULL
                                        ); '''

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_accounts_table)
    else:
        print("Error! cannot create the database connection.")


def new_account():
    create_connection(r"C:")
