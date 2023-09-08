import random as rd

print("#" *40)
print("Penalty Shoot Out Game\n")
print("Rule:")
print("* your have to enter number of the direction to shoot *")
print("1. Left")
print("2. Center")
print("3. Right")
print("-" * 40)

direction=rd.randrange(1,4)
# print(direction)
shoot_d=int(input("Shoot >> "))

if shoot_d >3 :
    print("Wrong Input!!!")
else:
    if direction == shoot_d:
        print("No Goal !")
    else:
        print('Goal! ' * 10)
