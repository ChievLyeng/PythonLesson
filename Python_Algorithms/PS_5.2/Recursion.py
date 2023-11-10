def binsearch(low,high,x,s) :
    if low > high : 
        return 0
    else :
        mid = (low + high) // 2
        if x == s[mid] : 
            return 1
        elif x < s[mid] :
            return 1 + binsearch(low,mid - 1,x,s)
        else :
            return 1 + binsearch(mid + 1,high,x,s)
        
def solve(n,m,s,x) :
    total = 0
    for i in range(m) :
        total += binsearch(0, n -1 ,x[i],s)
    print(total)

N,M = map(int,input().split())
S = list(map(int,input().split()))
X = list(map(int,input().split()))
solve(N,M,S,X)