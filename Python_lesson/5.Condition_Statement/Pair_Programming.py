age=int(input("Enter your age            : "))
height=int(input("Enter your height (cm) : "))

if age <= 65 and height >=110:
    print("You can enter...")
if age >65:
    print("Sorry you are over age!!!")
if height<110:
    print("Sorry your are under height!!!")
if age > 65 and height<110:
    print("Sorry you are not meet our standard yet!!!")