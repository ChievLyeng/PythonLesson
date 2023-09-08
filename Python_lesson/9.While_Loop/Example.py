#break and continue keyword

# i=0
# while i<3:
#     i+=1
#     print("Welcome to everyone!!")
#     if i==1:
#         break
# print("We're glad to see you")
# print(i)
#
# j=0
# while j<3:
#     j+=1
#     if j>1:
#         continue
#     print("Welcome to AnB")
# print("We're the champion")
# print(j)
#
#
# for i in range(3):
#     continue
#     print("welcome to Korea!")
# print("We're AnB students.")
# print(i)
#
# i=0
# while i<3:
#     i+=1
#     continue
#     print("welcome to Korea!")
# print("We're AnB students.")
# print(i)

print("-"*30)

# i=0
# while i<5:
#     print("Welcome to my heart!")
#     i+=1

print("rock paper scissor")
print("-"*30)

# selected=None
# while selected not in ["Rock","Paper","Scissors"]:
#     selected = input("Choose between Rock, Paper, Scissors >> ")
# print("The selected value is : ", selected)

# under_construction=True
# while under_construction:
#     response= input("Has the construction been completed : ")
#     if response == "yes" or response == "YES":
#         under_construction=False
#
# print("You have escaped the loop !")

print("Password login")
print("-"*30)

# pwd=""
# while pwd != "pythonisfun":
#     pwd=input("Enter Password : ")
# print("Login Successful!")


print("Sum")
print("-"*30)

# total=0
# answer="yes"
# while answer == 'yes':
#     number =int(input("Please enter numbers : "))
#     total+=number
#     answer=input("continue? (yes/no) : ")
# print("The sum is : ",total)

# st="Programming"
# for ch in st:
#     if ch  in ['a','e','i','o','u']:
#         break
#     print(ch)
# print("The end")
#
#
# for ch in st:
#     if ch in ['a','e','i','o','u']:
#         continue
#     print(ch)
# print("The end")

for i in range(2,10):
    for j in range (1,10):
        print("{} x {} = {:1d},".format(i,j,i*j),end=" ")
    print()