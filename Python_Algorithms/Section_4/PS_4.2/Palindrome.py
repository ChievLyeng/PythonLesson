def is_palindrome(n) :
    r,m = 0,n

    while m > 0 :
        r *= 10
        r += m % 10
        m //= 10

    # if (n == r) :
    #     print("n :",n)
    #     print("r :",r)
    return n == r # if n == r it is a palindrome

def is_palindrome2(n) :
    s = str(n)
    r = s[::-1]
    
    return int(s) == int(r)

def solve(n,m) :
    cnt = 0
    for i in range(n,m + 1) :
        if (is_palindrome2(i)) :
            cnt += 1
    return cnt

n,m = map(int,input().split())

print(solve(n,m))