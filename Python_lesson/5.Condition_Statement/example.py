# print("-----------------Sequential statement----------------")
# num=100
# print("num = ",num)
# num=num + 100
# print("num = ",num)
# num+= 100
# print("num = ",num)
#
# print("-----------------Conditional statement----------------")
#
age=18
# if age < 20 :
#     print("youth discount")
# print("---------------------------------")
# #no output
age2=24
# if age2 <20 :
#     print("youth discount ")
#
# print(age2)
# if age2 < 20 :
#     print("youth age")
#     print("youth discount")
# print("welcome")
#
if age2 < 20 :
    print("hello")
    pass # use for skip block


print("-----------------Checking for value equality----------------")
my_id = "Lyeng"

# s=input("Enter your id : ")
# if s == my_id:
#     print("Varify successful ( Id Matches )")
# else:
#     print("Sorry Id not matches (pleas enter again )")
#
# print("-----------------Checking for multiple----------------")
# number=int(input("Enter number : "))
# if (number % 3) == 0 and (number % 5) ==0 :
#     print(number,"is a multiple of 3 and 5 ")
#
#
# print("-----------------Checking for even number----------------")
# n=int(input("Enter an integer : "))
# print("n = ",n)
# if n%2 == 0:
#     print(n,"is an even number .")
#
# print("-----------------Checking for string equality----------------")
# str1="aaa"
# str2="bbb"
# if str1 ==str2:
#     print("The two strings are the same.")
# if str1!=str2:
#     print("The two strings are not the same.")

# print("-----------------Determining pass or fail based on scores----------------")
# score=int(input("Enter your score : "))
# if score >= 90:
#     print("Congratulations.")
#     print("You passed.")
#     print("You can also get a scholarship.")
# if score < 50:
#     print("You are failed ")

print("-----------------Examples using logical operator----------------")
a=10
b=13
if (a % 2 == 0) and (b % 2 == 0):
    print("Both numbers are even numbers.")
if (a % 2 == 0) or (b % 2 == 0):
    print("One or more of the two numbers are even.")
