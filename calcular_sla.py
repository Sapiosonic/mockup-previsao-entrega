from datetime import datetime
import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


now = datetime.now()
hours = 0
sla = 18
working_hours = 8

# get the current date
def get_current_date():
    return now.strftime("%d-%m-%Y")

# get the current time
def get_current_time(current_time):
    current_time = now.strftime("%H:%M:%S")

    if(int(current_time[4]) > 0):
        if(int(current_time[6]) > 0):
            current_time = now.strftime("%H")
            current_time_int = int(current_time)
            return current_time_int + 1
    else:
        current_time = now.strftime("%H")
        current_time_int = int(current_time)
        return current_time

# calculate the Service Level Agreement time
def calculate_sla():
    full_hours = sla // working_hours
    minutes = (sla % working_hours) * 60 / 60
    
    return f"{full_hours}d {int(minutes)}h"

# retrieve data from DB
cursor.execute("SELECT * FROM parametrizacao ")

value = cursor.fetchall()

cursor.close()
connection.close()

print(value)

# source https://www.programiz.com/python-programming/datetime/current-time