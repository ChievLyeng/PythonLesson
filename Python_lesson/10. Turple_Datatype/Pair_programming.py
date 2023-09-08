num=(1,2,5,4,3,2,1,4,7,8,9,9,3,7,9,3,3)

print(num.count(3))
temp=list(num)
temp.sort()

print(num)
c=num[0]
i=1
count = i
while i < len(num):
    count += 1
    if num[i] != c:
        if num.count(num[i]) > num.count(c):
            c = num[i]
        elif num.count(num[i]) == num.count(c) and num[i]> c:
            c = num[i]
    i += 1
print(c)

