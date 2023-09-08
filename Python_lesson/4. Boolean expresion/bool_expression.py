print(bool(1))
print(bool(0))
print(bool(""))
print(bool(None))
print(bool(-1))
print(bool("hello"))

print("------------Comparison operator--------------------------------")
print("Result of 10 > 5 : ",10>5)
print("Result of  5 < 1 : ",5<1)
print("Result of 5 == 5 : ",5==5)
print("Result of 5 != 5 : ",5!=5)
print("Result of 'a' > 'b' : ",'a'>'b')

print("-------------Comparison operator-------------------------------")
n=int(input("Enter number : "))
print("Is this an even number ? ",n%2 == 0)

print("n = ",n)
print(0< n <200)

print("-------------Comparison operator-------------------------------")
print("aaa" == "aaa")
print("aaa" == "bbb")
print("aaa" != "aaa")
print("aaa" != "bbb")

print("------------Logical Operator--------------------------------")
x= True
y= False
print("x : True")
print("y : False")
print(("x and y : "),x and y)
print(("x  or y : "),x or y)
print(("Not x   : "),not x)
print(("Not y   : "),not y)

print("---------------Logial expression-----------------------------")
num2=int(input("Enter Integer : "))
result=num2>=0 and num2<=100 and num2%2==0
print("Is this Integer an even number within the range of 0 to 100 ? ",result)

print("---------------Logial expression-----------------------------")
num3=2023
res=(num3 % 4 == 0 and num3 % 100 !=0) or num3 % 4 == 0
print("Result : ", res)

print("---------------Is operator-----------------------------")
a=1
b=1.0
print("a = 1 , b = 1.0")
print("a == b : ",a==b)
print("a is b : ",a is b)

print("----------------In operator----------------------------")
print("aaa" in "aaa-bbb-ccc")
print("bbb" in "aaa-bbb-ccc")
print("ddd" in "aaa-bbb-ccc")

print("----------------Order of Operation---------------------")
x=int(input("Enter the first  number : "))
y=int(input("Enter the second number : "))
z=int(input("Enter the third  number : "))

avg=(x+y+z)/3
print("Average : ",avg)



