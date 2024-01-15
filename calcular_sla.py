from datetime import datetime, timedelta
import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

now = datetime.now()
day_of_week = now.weekday()
next_day_date = now.hour
# day_name = now.strftime("%A")
# print(day_name)
hours = 0
sla = 18
working_hours = 8
beginning = 8
end = 17

# get the current date
def get_current_date():
    return print(now.strftime("%d-%m-%Y"))

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
        return current_time_int

# calculate the Service Level Agreement time
def calculate_sla_in_days():
    full_hours = sla // working_hours
    minutes = (sla % working_hours) * 60 / 60
    
    return print(f"{full_hours}d {int(minutes)}h")

# calculate the hours worked
def calculate_hours_worked(now):
    current_time = get_current_time(now)
    if int(current_time) > 8 and int(current_time) < 17:        
        worked = current_time - beginning
        to_work =  end - current_time 
        remaining_sla = sla - worked
        day_of_week = now.strftime("%A")
        print('The total hours worked today:', worked)
        print('The hours left to work today:', to_work)
        print('The remaining SLA:', remaining_sla)
        print(day_of_week)

    if int(current_time) > 17:
        next_day_datetime = now + timedelta(days=1)
        next_day_date = next_day_datetime.date()
        print(f"Skipping to the next day: {next_day_date.strftime('%d-%m-%Y')}")
        
# call functions
get_current_date()
calculate_sla_in_days()
calculate_hours_worked(now)


# retrieve data from DB
# cursor.execute("SELECT * FROM parametrizacao ")

# value = cursor.fetchall()

# cursor.close()
# connection.close()

# print(value)

# source https://www.programiz.com/python-programming/datetime/current-time