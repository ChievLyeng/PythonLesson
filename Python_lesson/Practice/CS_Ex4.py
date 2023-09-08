#Exercise4

# a=int(input("Enter a : "))
# b=int(input("Enter b : "))
# c=int(input("Enter c : "))
# d=int(input("Enter d : "))
# x=int(input("Enter x : "))
# k=int(input("Enter k : "))
#
# if x>k:
#     print("f(x) : ",(a*x)**3 + (b*x)**2 + (c*x) - d)
# elif x==k:
#     print("f(x) : ",0)
# elif x<k:
#     print("f(x) : ", -(a*x) ** 3 + (b*x) ** 2 - (c*x) - d)



#Exercise5
class_held=int(input("Number of class held    : "))
class_attence=int(input("Number of attendance : "))

avg_attendenc=(100*class_attence)/class_held

if avg_attendenc>0 and avg_attendenc<75:
    print("Your attendance is",avg_attendenc,"% Your are not allow to take the exam!")
if avg_attendenc>=75 and avg_attendenc<=100:
    print("Your attendance is",avg_attendenc,"% Your can sit and take the exam.")