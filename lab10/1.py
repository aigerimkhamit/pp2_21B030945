import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Aigerim2004'
)

sql = 'select user_id, username, phonenumber from phonebook'

cursor = conn.cursor()
cursor.execute(sql)
all_rows = cursor.fetchall()
def insert_account(username, phonenumber):
    conn = None
    user_id = None
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='Aigerim2004'
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO phonebook (username, phonenumber) VALUES (%s, %s) RETURNING user_id", (username, phonenumber))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
    return user_id

name = input()
number = int(input())
insert_account(name, number)
for row in all_rows:
    print(row)
cursor.close()
conn.close()