# import calendar as c
# yy=2023 #year
# mm=7  #month
#
# print(c.month(yy,mm))

print("\n                       Aging Rate Calculator")
print("-" * 70)

# age=("0-9","10-19","20-29")
population_a=(100,150,230,120,180,100,140,95,81,21,4)
population_b=(300,420,530,420,400,300,40,5,1,1,1)

# print("Age       : ",age)
print("Village A : ",population_a)
print("Village B : ",population_b)
print("-" * 70)

olda=sum(population_a[7:11])
oldb=sum(population_b[7:11])
print("Population of old people in village a :",olda)
print("Population of old people in village b :",oldb)

print("-" * 70)
totala,totalb=sum(population_a),sum(population_b)
print("Total population of village a :",totala)
print("Total population of village b :",totalb)

print("-" * 70)
ratea,rateb=olda/totala,oldb/totalb

print("The aging degrees of village A and B are {:5.3f} and {:5.3f} each".format(ratea,rateb))