import psycopg2
import os

def connect_db():
    conn = psycopg2.connect(database=os.environ.get('PGDATABASE'),
                            host=os.environ.get('PGHOST'),
                            user=os.environ.get('PGUSER'),
                            password=os.environ.get('PGPASSWORD'),
                            port=os.environ.get('PGPORT'))

    return conn.cursor()


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
    cursor.execute(f'''SELECT EXISTS(SELECT FROM km23_users WHERE id = {user_id});''')
    return cursor.fetchone()[0]


def get_user_schedules():
    return None


if __name__ == '__main__':
    conn = psycopg2.connect(database=os.environ.get('PGDATABASE'),
                            host=os.environ.get('PGHOST'),
                            user=os.environ.get('PGUSER'),
                            password=os.environ.get('PGPASSWORD'),
                            port=os.environ.get('PGPORT'))

    cursor = conn.cursor()
    # output = []
    # user_id = 414283157
    # group = 'km23_users'
    # cursor.execute(f'''SELECT groups FROM {group} WHERE id = {user_id};''')
    # result = cursor.fetchone()[0]
    # print(result)
    # groups = result.split()
    # for i in groups:
    #     cursor.execute(f"""SELECT * FROM {i}
    #     WHERE (week = '{0}')
    #     ORDER BY weekday, time;""")
    #     output.append(cursor.fetchall())


    # cursor.execute(f"""SELECT * FROM {groups}
    # WHERE (week = '{0}')
    # ORDER BY weekday, time;""")
    # output.append(cursor.fetchall())
    
    # print(output)
    conn.commit()
    cursor.close()
    conn.close()