import psycopg2
import os


def query_day(weekday: int, week: int, cursor) -> list:
    """returns list of tuples(all lessons) structured:
    Day, week, datetime(hour, min), lesson_name, lesson_type, prof_name, link
    """
    cursor.execute(f"""SELECT * FROM km23
        WHERE (weekday = '{weekday}' AND week = '{week}')
        ORDER BY time;""")
    return cursor.fetchall()


def query_week(week: int, cursor) -> list:
    """returns list of tuples(all lessons) structured:
    Day, week, datetime(hour, min), lesson_name, lesson_type, prof_name, link
    """
    cursor.execute(f"""SELECT * FROM km23
        WHERE (week = '{week}')
        ORDER BY weekday, time;""")
    return cursor.fetchall()


def verify_user(user_id, cursor):
    cursor.execute(f'''SELECT EXISTS(SELECT FROM km23_users WHERE user_id = {user_id});''')
    return cursor.fetchone()[0]


if __name__ == '__main__':
    conn = psycopg2.connect(database=os.environ.get('PGDATABASE'),
                            host=os.environ.get('PGHOST'),
                            user=os.environ.get('PGUSER'),
                            password=os.environ.get('PGPASSWORD'),
                            port=os.environ.get('PGPORT'))

    cursor = conn.cursor()
    
    conn.commit()
    cursor.close()
    conn.close()