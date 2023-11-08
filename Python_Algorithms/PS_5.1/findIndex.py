def binsearch(low,high,x,s) :
    if low > high : 
        return -1
    else :
        mid = (low + high) // 2
        if x == s[mid] : 
            return mid
        elif x < s[mid] :
            return binsearch(low,mid - 1,x,s)
        else :
            return binsearch(mid + 1,high,x,s)
        
def solve(n,m,S,X) :
    for i in range(m) :
        j = binsearch(0,n-1,X[i],S)
        print(j,end=" ")
    print()

N,M = map(int,input().split())
S = list(map(int,input().split()))
X = list(map(int,input().split()))
solve(N,M,S,X)