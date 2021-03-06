# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

def LeapYear(year):
    if year % 4 <> 0:
        return 0
    else:
        if year % 100 <> 0:
            return 1
        else:
            if year % 400 <> 0:
                return 0
            else:
                return 1

def DaysinMonth(year,month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 4 or month == 6 or month == 9 or month == 11:
            return 30
        else:
            return 28 + LeapYear(year)

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < DaysinMonth(year,month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

print daysBetweenDates(1900,1,1,1901,1,1)

def Sundays_on_the_first(year1,month1,day1,year2,month2,day2,start_day_of_week,target_day_of_week):
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    count = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        if day1 == 1 and start_day_of_week == target_day_of_week:
            count += 1
        year1, month1, day1 = nextDay(year1, month1, day1)
        start_day_of_week = (start_day_of_week + 1) % 7
    return count

print Sundays_on_the_first(1901,1,1,2000,12,31,1,6)
