print("\n        BSNL Company    ")
print("-"*30)
rate=0
print("Customer Category")
print("1. Commercial")
print("2. Institutional")
print("3. Domestic")
print("-"*30)
customer=int(input("Please Enter number of customer type : "))

if customer <=0 or customer>4:
    print("Invalid Input!!!")
else:
    if customer==1:
        unit = float(input("Enter units : "))
        if unit == 5000:
            rate=1500
        elif unit>5000 and unit <10000:
            over=(5000-unit)*0.25
            rate=1500 +over
        elif unit>10000:
            over=(10000-unit)*0.20
            rate=(5000-unit)*0.25 +over


    elif customer==2:
        unit = float(input("Enter units : "))
        if unit == 5000:
            rate = 1800
        elif unit > 5000 and unit < 10000:
            over = (5000 - unit) * 0.30
            rate = 1500 + over
        elif unit > 10000:
            over = (10000 - unit) * 0.28
            rate = (5000 - unit) * 0.30 + over



    elif customer == 3:
        unit = float(input("Enter units : "))
        if unit == 5000:
            rate = 1500
        elif unit > 5000 and unit < 10000:
            over = (5000 - unit) * 0.25
            rate = 1500 + over
        elif unit > 10000:
            over = (10000 - unit) * 0.20
            rate = (5000 - unit) * 0.25 + over

print("Rate : ",rate)