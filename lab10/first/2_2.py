# upload data from csv file
import psycopg2
import csv

def insert_user_list(user_list):
    sql = """
    insert into MyPhoneBook(username, phonenumber) values (%s, %s);
    """
    conn = None
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='Aigerim2004'
        )
        cur = conn.cursor()
        cur.executemany(sql, user_list)
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

with open('my.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    # for row in csv_reader:
    insert_user_list(csv_reader)

