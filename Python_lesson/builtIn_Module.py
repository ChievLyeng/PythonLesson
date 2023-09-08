from datetime import * #it mean to import all variables,functions and classes
today =date.today()
print(today)


import datetime
print(datetime.datetime.now())

start_time= datetime.datetime.now()
print(start_time.replace(month=10, day=22)) #replace date

Today=datetime.date.today()
print(Today)
#print(dir(datetime))

#time module-----
import time
seconds= time.time()
print("Time after epoch = ",seconds)

unix_timestamp =time.time()
local_time = time.localtime(unix_timestamp)
print(local_time)

print(time.strftime("%Y-%m-%d %H-%M-%S"),local_time)


#math_Module
import math as m

a=m.pow(3,2)
print("{:4.2f}".format(a))

b=m.fabs(-99)  #bomleng tv positive
print(b)

c=m.ceil(2.1) #bongkot lerng
print(c)

d=m.ceil(-2.1) #bongkot negative jos
print(d)

print(m.floor(2.1)) #bongkot jos

print(m.log(2.17828))

print(m.log(100,10))

print(m.exp(2))

print(m.degrees(1.57))
print(m.radians(89.9543))

print(m.cos(90))
print(m.sin(90))
print(m.sin(0))
print(m.sin(m.pi/2))
print(m.cos(m.pi/2))

#random module

import random as rd

print(rd.random())
print(rd.random())
print(rd.randrange(1,7))
print(rd.randrange(0,10,2))  # return an int that is a multiple of 2 from 0 to 10
print(rd.randint(1,10)) # return random int

numlist=[10,20,30,40,50]
rd.shuffle(numlist) # return the sequence with its elements shuffled in a different order each time
print(numlist)

f=list(range(1,11))
rd.shuffle(f)
print(f)

print(rd.choice(numlist)) #extracts a random element from the given sequence

print(rd.sample(numlist,3)) #return elements randomly the number of elements to be returned can  be specified

x=list(range(1,11))
y=rd.sample(x,3)
print("Random integer from 1 to 10 :" ,y)

