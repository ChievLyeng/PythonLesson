print("\nLoop-Statement")

#for loop
for i in range(5):
    print("Welcome to everyone!!!")

#while loop
i=0
while i<5 :
    print("Welcome to AnB school!")
    i+=1


for ch in "Hello":
    print(ch,end=" ")

print("My name is ",end=": ")
print("David")

numbers=[10,20,30,40,50]
s=0
for n in numbers:
    s+=n
print("sum of list : ",s)

for _ in range(3):
    print("I love u")

for _ in [1,2,3,4,5]:
    print("wo xi huan ni")

for i in [10,20,30]:
    print(" wo xiang ni")

c=list(range(4))
print(c)
for _  in c:
    print("ni xiang wo ma")

#range function

print(list(range(5)))
print(list(range(0,5)))
print(list(range(0,5,1)))
print(list(range(0,10,2)))
print(list(range(0,5,2)))
print(list(range(5,0,-2)))
print(list(range(10,0,-4)))
print(list(range(5,-1,-1)))
print(list(range(-1,5,2)))
s2=0
for i in range(1,11):
    s2+=i
print("The sum of 1 to 10 : ",s2)

x=int(input("Enter a number : "))
fact=1
for i in range(1,x+1):
    fact = fact*i
print(str(x) + "! = ",fact)

for i in range(0,x+2):
    print("hello")
