"""
create or replace procedure insert_user_list(name, number)
$$
begin
    insert into myphonebook(myphonebook.username, myphonebook.phonenumber) values (name, number);
end;
$$
language plpgsql;
"""

import psycopg2
list = (('Aigerim', '87012465854'), ('Medina', '87476227404'), ('Nurailya', '87781604480'))
def insert_users(list):
    conn = None
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='Aigerim2004'
        )
        cur = conn.cursor()
        cur.executemany('call insert_user_list(%s, %s)', list)
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
insert_users(list)