s0=87
s1=84
s2=95
s3=67
s4=88
s5=94
s6=63

score_list=[s0,s1,s2,s3,s4,s5,s6]
print(score_list)
print(score_list[0],score_list[3])

bk=["Vathanaka","Chanthea","Bunchai","Noron"]
print(bk[0],"is the famous football player in Cambodia!")
print(bk[1],"is the best youngest football player in Cambodia currently.")

ppc=[]
ppc.append("Takaki") #add item to empty list
ppc=ppc+["pisoth"]   #add item to empty list
print(ppc)

mixed_list=[100,200,'apple',400]
print(mixed_list)

list4=list(range(1,11)) #define list by range function
print(list4)

n_list=[11,22,33,44,55,66]
print(n_list)
print("Length of list : ",len(n_list))
print("first index element : ",n_list[0])
print("Last index element  : ",n_list[-1])

#Slicing list using index
print(n_list[:])
print(n_list[0:4])
print(n_list[0:3])
print(n_list[:5])
print(n_list[-6:])
print(n_list[5::-1])


person1=["Lyeng",20,1,170.0,85.0]
person2=["Jonh smith",25,1,170.0,70.]
person_list=person1 + person2 #concatenating list usnig + operator
print(person_list)

#checking value in list with in operator
print(11 in n_list)
print(50 in n_list)
print(22 not in n_list)
print(32 not in n_list)

#append Method
a_list=['a','b','c','d','e']
a_list.append("f") #add item to the last index of list
print(a_list)

n_list.append(77)
print(n_list)

#extend Method
list1=['a','b','c']
list2=[1,2,3]
list1.extend(list2) # add the items of list2 after items of list1
print(list1)

list1.extend("d")
#list1.extend(1) #extend cannot add numeric
#list1.append("b",'c')  # append can only take 1 agrument
print(list1)

#insert Method
slist=['David',178.9,'Jonh',173.5,'Jane',176.1]
print(slist)
slist.insert(4,"Petter")
slist.insert(5,168.1)
print(slist)

#remove Method
print(n_list)
n_list.remove(66)
print(n_list)

if 55 in n_list:
    print("55 is in n_list")
    print(n_list)
    n_list.remove(55)
    print("55 is removed from n_list")
    print("55 is not in n_list")
    print(n_list)

bk.append("sambath")
print(bk)

if "sambath" in bk:
    bk.remove("sambath")
print(bk)

print(n_list)
n=n_list.pop() # return and remove last item in the list
print("n = ",n)
print("n_list = ",n_list)

del n_list[2] # keyword use to delete item of list by index
print("33 is deleted ",n_list)


# sort Method
n_list.extend([10,20,30,40])
print(n_list)
n_list.sort()
print(n_list)
n_list.sort(reverse=True) # revers sort
print(n_list)
print("Length of n_list : ",len(n_list))
print("Max of n_list : ",max(n_list))
print("Min of n_list : ",min(n_list))
print("Sum of n_list : ",sum(n_list))

print(any(n_list))
b_list=[0,'']
print(any(b_list))

