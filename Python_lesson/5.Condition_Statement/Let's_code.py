import random as rd
n1=rd.randrange(1,10)
n2=rd.randrange(1,10)
n3=rd.randrange(1,10)

#n1,n2,n3 =2,3,9
a,b,c=input("Enter a ,b ,c : ").split(" ")
a=int(a)
b=int(b)
c=int(c)
n=0

if a==n1 or a==n2 or a==n3:
    n+=1
if b==n2 or b==n2 or b==n3:
    n+=1
if c==n1 or c==n2 or c==n3:
    n+=1
if n==3:
    print("You won the lottery ...")
else:
    print("It's unlucky this time try later...")

    print("The Lottery number is : ",n1,n2,n3)