year=int(input("Enter Year : "))
leap_year= (year % 4 == 0 or year % 400 ==0) and year % 100 !=0
if leap_year == True:
    print(year,"is leap year")
else :
    print(year, "is not leap year")