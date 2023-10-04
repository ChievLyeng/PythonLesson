import time

#solution 1

# def findDivisors (N) :
#     cnt = 0
#     for i in range(1,N+1) :
#         if  N % i == 0 :
#             cnt += 1
#     return cnt

# start =time.time()
# N = int(input("Enter N : "))
# print("{} have {} divisors".format(N,findDivisors(N)))

# end = time.time()
# print("Duration of execution : {:.2f} s".format(end - start))

# --------------------------------------------------------------

#solution 2
def findDivisors ( N ) :
    cnt = 0
    sqrtn = int(N ** 0.5)
    for i in range(1 , sqrtn + 1) :
        if N % i == 0 :
            cnt += 2
    if sqrtn * sqrtn == N :
        cnt -= 1

    return cnt

start =time.time()
N = int(input("Enter N : "))
print("{} have {} divisors".format(N,findDivisors(N)))

end = time.time()
print("Duration of execution : {:.2f} s".format(end - start))