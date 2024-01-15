import datetime
from datetime import timedelta

# Define the working hours
working_hours_start = datetime.time(8, 0, 0)
working_hours_end = datetime.time(17, 0, 0)

# Define the holidays
holidays = [
    datetime.date(2024, 1, 1),  # New Year's Day
    datetime.date(2024, 12, 25),  # Christmas Day
    datetime.date(2024,1,17) # fake holiday for test purposes
    # Add more holidays as needed
]

def calculate_deadline(sla_hours):
    working_hours_start = datetime.time(8, 0, 0)
    working_hours_end = datetime.time(17, 0, 0)
    
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.time()
    current_date = current_datetime.date()
    
    remaining_hours = 0
    to_work = 0
    
    if current_time >= working_hours_start and current_time <= working_hours_end:
        remaining_hours = (working_hours_end.hour - current_time.hour) + (working_hours_end.minute - current_time.minute) / 60
        
        to_work = remaining_hours - sla_hours
        if to_work < 0:
            to_work = 0
        
        if current_time > working_hours_end:
            current_date += timedelta(days=1)
            remaining_hours = 0
    
    delivery_date = current_date
    while remaining_hours < sla_hours:
        delivery_date += timedelta(days=1)
        if delivery_date.weekday() >= 5:  # Saturday is 5 and Sunday is 6
            continue  # Skip weekends
        
        if delivery_date in holidays:
            continue  # Skip holidays
        
        remaining_hours += 8  # Add 8 working hours per day
    
    delivery_time = datetime.datetime.combine(delivery_date, working_hours_start) + timedelta(hours=remaining_hours)
    estimated_deadline = delivery_time.strftime("%d/%m/%Y %Hh")
    
    return estimated_deadline

# Example usage
sla_hours = 22  # Service Level Agreement in hours

estimated_deadline = calculate_deadline(sla_hours)
print("Estimated deadline:", estimated_deadline)


'''
    To estimate a deadline for a given Service Level Agreement (SLA) in hours, where you have a
    specified number of hours to resolve a problem, working from 8 AM to 5 PM and excluding weekends
    and holidays, you can use the following approach:

        1. Calculate the remaining working hours in the current day from the current time until the end
        of the working day (5 PM).

        2. Calculate the number of working days required to complete the remaining hours, considering 
        weekends and holidays.

        3. Calculate the expected resolution date and time by adding the working days to the current date 
        and time, excluding weekends and holidays, and adjusting for the remaining working hours.

        4. Return the estimated deadline.
'''