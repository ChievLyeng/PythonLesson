print("------------------If Else Statement----------------------------")
# score=int(input("Enter your score : "))
# if score > 60:
#     print("You passed.")
#     print("Get a scholarship, too.")
# else:
#     print("You failed.")

print("----------------------------------------------")
# x=input("Enter the first integer : ")
# if x.isdigit()==True:
#     x=int(x)
#     print("Input datatype : ",type(x))
# else:
#     print("X is not a numeric character.")

print("----------------------------------------------")
# id="ilovepython"
# s=input("Enter your ID : ")
# if s == id:
#     print("Welcome")
# else:
#     print("ID is incorrect")

print("----------------------------------------------")
import random as rd

# print("Let's start the coin toss game ")
# coin = rd.randrange(2) # it stop on 2 (default start is 0)
# print(coin)
# if coin == 0:
#     print("Front")
# else:
#     print("Back")
#
# print("Game Over >>")
print("-------------------Nested conditional Statement---------------------------")

# num=int(input("Enter an Integer : "))
# if num >= 0:
#     if num == 0:
#         print("It's 0")
#     else:
#         print("It's a positive number.")
# else:
#     print("It's a negative number.")
print("----------------------------------------------")
# num2=int(input("Enter number : "))
# if num2 < 0:
#     print(num2,"is a negative number.")
# else:
#     print(num2,"is not a negative number.")
#     if num2 % 2 == 0:
#         print(num2,"is an even number.")
#     else:
#         print(num2,"is an odd number.")

print("----------------------------------------------")
# num3=int(input("Enter Integer : "))
#
# if num3 > 0:
#     print("It's a positive number.")
# elif num3==0:
#     print("It's zero.")
# else:
#     print("It's a negative number.")
print("----------------------------------------------")
# print("#" *50)
# print("It's Lyeng's fruit shop")
# print("1: Apple (Price : 5,000 won")
# print("2: Grape (Price : 6,000 won")
# print("3: Melon (Price : 8,000 won")
# print("4: Orange (Price : 2,000 won")
# print("5: Cherry (Price : 9,000 won")
# print("#" *50)
#
# total_price = 0
# order = int(input("Enter number of Menu  (1-5)  >> "))
# count = int(input("Enter number of items (1-10) >> "))
#
# if order == 1:
#     fruit ="Apple"
#     price = 5000
# elif order == 2:
#     fruit = "Grape"
#     price = 6000
# elif order == 3:
#     fruit = "Melon"
#     price = 8000
# elif order == 4:
#     fruit = "Orage"
#     price = 2000
# else:
#     fruit = "Cherry"
#     price = 9000
# total_price=price*count;
# print("Your fruit is : ", fruit)
# print("Price of the selected fruit is : ",price)
# print("Number of items is : ",count)
# print("Total amount       : ",total_price," won")
#
# money=int(input("Please put the money in >> "))
# if money<total_price:
#     print("Sorry not enough money")
# else:
#     change=money -total_price
#     print("Got",money," won",)
#     print("The change is ",change," won")

print("----------------------------------------------")

# my_id="anb"
# pwd="anb004"
# str1 =input("Enter your ID       : ")
# str2 =input("Enter your password : ")
#
# if str1 == my_id and str2 == pwd:
#     print("Welcome to Above and Beyond school ")
# elif str1 != my_id:
#     print("Your ID is incorrect!")
# else:
#     print("Your password is incorrect!")
print("----------------------------------------------")
# print("*" * 10, "GPA Calculator","*" *10)
#
# point=float(input("Enter your score : "))
# if point >= 90:
#     grade = "A"
# if point < 90 and point >=80:
#     grade= "B"
# if point < 80 and point >=70:
#     grade= "C"
# if point < 70 and point >= 60:
#     grade= "D"
# if point < 60 and point >= 50:
#     grade= "E"
# if point<50:
#     grade= "F"
#
# print("Your Grade : ",grade)

print("----------------------------------------------")
print("*" * 10, "GPA Calculator","*" *10)

point=float(input("Enter your score : "))
if point >= 90:
    grade = "A"
elif point < 90 and point >=80:
    grade= "B"
elif point < 80 and point >=70:
    grade= "C"
elif point < 70 and point >= 60:
    grade= "D"
elif point < 60 and point >= 50:
    grade= "E"
else:
    grade= "F"

print("Your Grade : ",grade)