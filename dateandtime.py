import time;
import calendar;
from datetime import date, datetime, timedelta
from calendar import monthrange

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


def print_time():
    return "Time: %f " %  time.time()

print(print_time())


def date_today():
    return datetime.today().strftime('%Y-%m-%d')

print("Date Today", date_today())


def date_yesterday():
    return datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

print("Date Yesterday", date_yesterday())


def convert_str_datetime(str):
    return date(*map(int, str.split('-')))

bdate = convert_str_datetime('1994-08-26')
print('Convert String to DateTime', bdate)

def calculate_age(bdate):

    today = date.today()
    return today.year - bdate.year - ((today.month, today.day) < (bdate.month, bdate.day))

print("Calculate Age", calculate_age(bdate))


def get_day_of_week(str):

    date_string = convert_str_datetime(str)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 

    return days[date_string.weekday()]

print("Day of the Week", get_day_of_week('2020-01-20'))

def get_number_of_days(date_str):
    
    year, month, day = (int(i) for i in date_str.split('-'))

    return monthrange(year, month)[1]

print("Number of days in a month", get_number_of_days('2020-01-20'))