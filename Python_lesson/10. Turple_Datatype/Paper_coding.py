t1="d","e","f","g"
t2=("a","b","c")
t3=("d","e","g")

print(t1==t2)
print(t1>t3)
print(t1 < t3)
print(t2 + t3)
print([t2 + t3])
print(t1)

d_record=(100,121,120,130,140,120,122,123,190,125)
print(d_record)
list1=[]
i=1
# for i in range(len(d_record)):
while i in range(len(d_record)):
    if d_record[i] < d_record[i-1]:
        list1.append(d_record[i])
    i+=1
print("The value of three day reduced sale are :",list1)



