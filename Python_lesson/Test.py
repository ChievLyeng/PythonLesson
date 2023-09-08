matrix1 = [[1, 2, 3],   [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
lst=[]

print("1) Matrix1 + Matrix2")
print("2) Matrix1 - Matrix2")
print("3) Matrix1 * Matrix2")
print("4) Press other keys to exit.")
print("="*30)

try:
    choice=int(input("Enter your choice 1-4 : "))
except:
    print("Hello kon papa!")

print("you have : matrix 2 ")
for i in range(len(matrix1)):
    for j in range(len(matrix2[i])):
        print(matrix1[i][j],end=" ")
    print()

print("you have : matrix 2 ")
for i in range(len(matrix2)):
    print(matrix2[i])


#addition
if choice == 1 :
    print("Matrix1 + Matrix2")
    for i in range(len(matrix1)):
        line = []
        for j in range(len(matrix2)):
            line.append(matrix1[i][j] + matrix2[i][j])
        lst.append(line)

    for i in range(len(lst)):
        print(lst[i])

#substraction
elif choice == 2 :
    print("Matrix1 - Matrix2")
    for i in range(len(matrix1)):
        line = []
        for j in range(len(matrix2)):
            line.append(matrix1[i][j] - matrix2[i][j])
        lst.append(line)

    for i in range(len(lst)):
        print(lst[i])

#multiplication
elif choice == 3 :
    # a=[]
    b=[]
    c=[]
    print("Matrix1 * Matrix2")
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            # print(matrix2[i][j], end=" ")
            # b.append(matrix2[i][j])
            d=[]
            for k in range(len(matrix1)):
                # print("M1",matrix1[i][k],end=" ")
                # a.append(matrix1[i][k])
                # print(matrix1[i][k],matrix2[k][j])
                d.append(matrix1[i][k]*matrix2[k][j])
            c.append(d)

    result = []
    for i in range(len(c)):
        s=sum(c[i])
        result.append(sum(c[i]))

    print(result)



