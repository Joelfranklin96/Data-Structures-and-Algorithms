not_leap = [31,28,31,30,31,30,31,31,30,31,30,31]
leap = [31,29,31,30,31,30,31,31,30,31,30,31]

def leap_year(year):
    if year %4 == 0:
        return True
    else:
        return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    # Calculating the difference in days between year1 and year2 assuming month1 = month2 = day1 = day2 = 1
    
    diff = 0
    for x in range(year1,year2):
        if leap_year(x):
            diff = diff + 366
        else:
            diff = diff + 365
    
    # Calculating the difference in days by taking into account the months and days specified.
    
    a = 0
    b = 0
    if leap_year(year1):
        for y in range(month1):
            a = a + leap[y]
        a = a + day1
    else:
        for y in range(month1):
            a = a + not_leap[y]
        a = a + day1
    if leap_year(year2):
        for y in range(month2):
            b = b + leap[y]
        b = b + day2
    else:
        for y in range(month2):
            b = b + not_leap[y]
        b = b + day2
        
        
    return diff + (b-a)


# Testing the function  

def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    print("The code is working correctly")
    
testDaysBetweenDates()
