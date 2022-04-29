# Implement updating data in the table (change user first name or phone)
import psycopg2

def update_user(id, username):
    sql = """
    update MyPhoneBook
    set username = %s
    where id = %s
    """
    conn = None
    updated_rows = 0
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='Aigerim2004'
        )
        cur = conn.cursor()
        cur.execute(sql, (username, id))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
update_user(12, 'Nazerke')