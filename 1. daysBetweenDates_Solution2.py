leap_mon = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
non_leap_mon = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

def nextDay(year, month, day):
    
    """Returns the year, month, day of next day of mentioned date"""
    
    if year%400 == 0:
        mon = leap_mon
    elif year%100 == 0:
        mon = non_leap_mon
    elif year %4 == 0:
        mon = leap_mon
    else:
        mon = non_leap_mon
    
    if mon[month]>day:
        return year,month,day+1
    else:
        if month == 12:
            return year+1,1,1
        else:
            return year,month+1,1
            
        
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
       and year2/month2/day2."""
       
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    
    return days

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
