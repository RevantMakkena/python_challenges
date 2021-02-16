# A year is leap year if its exacly divisible by 4, 400 & not by 100

def leap_year(year):
    if(year):
        if year % 4 == 0 and year % 100 != 0:
            return True

        if year % 4 == 0 and year % 400 == 0:
            return True

    return False


# %%  Other solutions
def leap_year_2(x):
    return x % 4 == 0 and (x % 100 != 0 or x % 400 == 0)
