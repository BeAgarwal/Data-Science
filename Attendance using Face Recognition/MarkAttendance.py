import psycopg2
from datetime import datetime
from datetime import date
import sys
import MariaConnection

def markAttendance(name, designation):
    conn = MariaConnection.connectwithPostgreSQL()
    date_object = date.today()
    now = datetime.now()
    time_object = now.strftime("%H:%M:%S")
    cur = conn.cursor()
    try:
        sql = "INSERT INTO attendance(name, date, time, designation) VALUES(%s, %s, %s, %s)"
        cur.execute(sql, (name, date_object, time_object, designation))
    except psycopg2.Error as e:
        print(f"Marking Attendance error: {e}")

    conn.commit()
    conn.close()
    return True
