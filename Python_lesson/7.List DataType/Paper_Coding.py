#Q1
prime_list=list(range(2,11))
print(prime_list)

#Q2

prime_list=list(range(1,11))
print(prime_list)
prime_list.append(11)
print(prime_list)
print("-" * 20)
#Q3

print("Multiplication")
list1=[3,5,7]
list2=[2,3,4,5,6]

for i in list1:
    for j in list2:
        print(str(i)+ " x "+str(j) + " = ",i*j)
        if j == 6:
            print("-" * 20)