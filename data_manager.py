import psycopg2
import config


def send_query(SQL):
    conn = None
    try:
        conn = psycopg2.connect(config.connect_str)
    except psycopg2.OperationalError as oe:
        print("Could NOT connect to database.")
        print(oe)
    else:
        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute(SQL)
            result = cursor.fetchall()
        if result:
            return result
    finally:
        if conn:
            conn.close()
