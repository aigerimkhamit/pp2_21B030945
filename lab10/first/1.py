# Design tables for PhoneBook.
import psycopg2

def create_tables():
    commands = (
        """
        CREATE TABLE MyPhoneBook (
            id serial PRIMARY KEY,
            username VARCHAR (50) UNIQUE NOT NULL,
            phonenumber VARCHAR (20) UNIQUE NOT NULL
        );
        """
    )
    conn = None
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='Aigerim2004'
        )
        cur = conn.cursor()
        cur.execute(commands)
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
        if conn is not None:
            conn.close()
create_tables()