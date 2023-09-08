print("\n Electricity Calculation")
print("-"*30)

new=float(input("Enter New number : "))
old=float(input("Enter Old number : "))
used=new-old
pay=0
over=0
print("Used Electricity : ",used)

if used >=1 and used <=100:
    pay=used*0.5
elif used>=101 and used<=200:
    over=((used-100)*1)
    pay=50+over
    print("Over 100 price : $",over)
elif used>=201 and used<=300:
    over = ((used - 200) * 1.5)
    pay = 150 +over
    print("Over 200 price : $", over)
elif used >= 301:
    over = ((used - 300) * 2)
    pay = 300 + over
    print("Over 300 price : $", over)
print("-"*30)
print("Total Payment  : $",pay)