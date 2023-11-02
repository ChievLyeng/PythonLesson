def is_palindrome2(n) :
    s = str(n)
    r = s[::-1]
    
    return int(s) == int(r)

def is_prime(n) :
    if n <= 1 :
        return False
    for i in range(2,int(n ** 0.5) + 1) :
        if n % i == 0 :
            return False
    return True

def solve(n,m) :
    cnt = 0
    for i in range(n,m + 1) :
        if is_palindrome2(i) and is_prime(i) : 
            cnt +=1
    return cnt

n,m = map(int,input().split())
print(solve(n,m))
# we use this solution 2 because the palindrome is less the prime
# this is faster than the first on because 
# the and operator does not call the is_palindrome when is_prime return false