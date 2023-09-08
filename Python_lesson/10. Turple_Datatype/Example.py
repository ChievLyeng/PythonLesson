colors =("red","green","blue")
print(colors)

numbers=(1,2,3,4,5)
print(numbers)

tup = (100)
print(tup)
print(type(tup))

tub=(100,) #use comma to define tuple if not it an integer
print(tub)
print(type(tub))

#packing
a=(1,2)
print(a[0])
print(a[1])

#unpacking
c=(3,4)
x,y=c
print(x)
print(y)

#sort tuple

tup=(1,2,4,5,6,7,3,9)
temp=list(tup)
temp.sort()
print(temp)

#range and sequence type
even_list=list(range(2,11,2))
print("even_list : ",even_list)

print(list(range(10)))
print(list(range(2,10)))
print(list(range(2,10,3)))

#tuple index
tup1=(1,1,1,1,2,3,3,4)
print(tup1[3])
print(tup1[-3])

#range index
ran=range(0,5,1)
print(ran[4])
print(ran[-2])

#slicing negative index
list5=[10,20,30,40,50,60,70,80]
print(list5[-7:-2])
print(list5[:-3])
print(list5[-8:])

#membership operator
print("10 is in list     : ",10 in list5)
print("10 is not in list : ",10 not in list5)

print(3 in tup1)
print(11 in ran)
print("a" in "aeiou")


#Len function
nations=["Korea","China","Russia","Malaysia"]
print("Last element of nations : ",nations[len(nations) - 1])

#count method
ran2 = range(0,5,1)
print(len(ran2))
print(ran2.count(2)) # count how many 2 appear in ran2

list5.append(10)
print(list5)
print("number 10 in list has : ",list5.count(10))

str1="hello world"
print(str1.count("l"))

#concatenate
list1=[11,22,33,44]
list2=[55,66]
print(list1)
print(list2)
print(list1 + list2)


print(tup + tup1)
print((tup+tup1).count(1))

#duplicate
list3=list1*2
print(list3)
list4=[1,2,3,4]*3
print(list4)

tup2=(1,2,3,4,5)*2
print(tup2)

str2="Lyeng "
print(str2 * 3)

ran=list(range(5)) *2
print(ran)

ran=tuple(range(5)) * 2
print(ran)

#ord built-in function

print(ord("C"))
print(ord("c"))
print(ord("D"))
print(ord("d"))

print("C" > "D")
print("C" < "D")

print("ABC" > "ABD")
print("ABC" < "ABD")

# is operator
list1=[10,20,30]
list2=[10,20,30]
print(list1)
print(list2)
#is operator compare the list id and it is not the same obj
# because it store in the different location

if list1 == list2:
    print("It's same .")
    if list1 is list2:
        print("It's same object.")
    else:
        print("It's different object.")
else:
    print("It's different")


# for str datatype, a table is used to store its location,
# and if the same string is assigned, it refers to the same location
str1="ABC"
str2="ABC"

if str1 == str2:
    print("It's same .")
    if str1 is str2:
        print("It's same object.")
    else:
        print("It's different object.")
else:
    print("It's different")


print(id(list1), " vs ", id(list2))
print(id(str1), " vs ", id(str2))


n=100
print(id(100))
print(id(n))

m=n
print(id(n))
print(id(m))

m=200
n=200
print(id(n))
print(id(m)) # if the value is the same it also has the same id

m=240
n=250
print(id(n))
print(id(m))
# if it has different value it also has different id
# because it store in different storage

