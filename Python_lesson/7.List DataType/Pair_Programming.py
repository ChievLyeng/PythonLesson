list=["abc","bcd","bcdefg","abba","cddc","oqb"]
# a=len(list[0])
# b=len(list(1))
# print(len(list[0]),len(list[1]),len(list[2]),len(list[3]),len(list[4]))
# a=len(list[0])
# b=len(list[1])
# c=len(list[2])
# d=len(list[3])
# e=len(list[4])
# f=len(list[5])
# print(a,b,c,d,e)

# if a<b and a<c and a<d and a<e:
#     print(list[0])
# elif b<a and b<c and b<d and b<e:
#     print(list[1])
# elif c < a and c < b and c < d and c < e:
#     print(list[2])
# elif d < a and d < c and d < b and  d < e:
#     print(list[3])
# elif e < a and e < b and e < c and e < d:
#     print(list[4])

# list2=[a,b,c,d,e]
# for i in list2:
#     print("len of list : "+str(i))
#
# if a>b and a>c and a>d and a>e:
#     print(list[0])
# elif b>a and b>c and b>d and b>e:
#     print(list[1])
# elif c > a and c > b and c > d and c > e:
#     print(list[2])
# elif d > a and d > c and d > b and  d > e:
#     print(list[3])
# elif e > a and e > b and e > c and e > d:
#     print(list[4])

# list.sort(key=len)
# print(list)
# min_len=3
# for i in list:
#     if len(i) == min_len:
#         print(i)

shortes=list[0]
longest=list[0]

for i in list:
    if len(i) < len(shortes):
        shortes=i
    elif len(i) > len(longest):
        longest=i
print(shortes)
print(longest)

list.sort(key=len)
print(list)
