def MultiplesOfNumber(number:int,dividednumber:int)->bool:
    if (number % dividednumber==0):
        return True
    return False

year = int(input('Enter Leap Year:'))
is_leap_year_400 = MultiplesOfNumber(year,400)
is_leap_year_100 = MultiplesOfNumber(year,100)
is_leap_year_4 = MultiplesOfNumber(year,4)
if( is_leap_year_400 and is_leap_year_100 ):
    print (f'{year} -> True')
elif( (not is_leap_year_400 and not is_leap_year_100) and is_leap_year_4 ):
    print(f'{year} -> True')
else:
    print(f'{year} -> False')
