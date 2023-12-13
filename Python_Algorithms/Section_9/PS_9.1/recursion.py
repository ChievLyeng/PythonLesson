def solve(a,b,m) :
    if b == 1 :
        return a % m
    else :
        c = solve(a, b//2,m)
        if b % 2 == 0 :
            return  (c * c) % m
        else :
            return (a * c * c) % m
        
A, B, M = map(int,input().split())
print(solve(A, B, M))