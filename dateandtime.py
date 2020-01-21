import time;
import calendar;


def get_current_time():
    return time.localtime(time.time())

def format_time():
    localtime = get_current_time()
    formattedtime = time.asctime(localtime)
    return formattedtime

print("Current Time", format_time())


def generate_calendar(year, month):
    cal = calendar.month(year, month)
    return cal

print(generate_calendar(2020,1))