# Function Definition
def is_leap_year (year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Function Call
obj1 = is_leap_year (2013)
print (obj1)
obj2 = is_leap_year (2012)  # 2012 is leap year
print (obj2)





"""---OR---"""





# Function Definition
def is_this_leap_year (year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Function Call
obj3 = is_this_leap_year (2016) # 2016 is leap year
print (obj3)
obj4 = is_this_leap_year (2018)
print (obj4)