name=input("Your name     : ")
h=float(input("Height(cm) : "))
w=float(input("Weight(kg) : "))
h/=100
bmi=w/h **2

print("BMI = ","{:2.2f}".format(bmi))
if bmi<18.5:
    print("Your are Underweight please eat more...")
if bmi>=18.5 and bmi <=24.9:
    print("Your are Ok !")
if bmi>=25 and bmi<=29.9:
    print("Your are overweight please do some excersise...")
if bmi>30:
    print("Your are Obesity....!")