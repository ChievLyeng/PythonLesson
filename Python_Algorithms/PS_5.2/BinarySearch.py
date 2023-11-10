def binsearch(x,n,s) :
    low,high = 0 , n -1 
    cnt = 0
    while low <= high : 
        mid = (low + high) // 2
        cnt += 1
        if x == s[mid]: 
            return cnt 
        elif x < s[mid] :
            high = mid -1 
        else: # x > s[mid] :
            low = mid + 1
    return cnt

def solve(n,m,s,x) :
    total = 0
    for i in range(m) :
        total += binsearch(x[i],n,s)
    print(total)

N,M = map(int,input().split())
S = list(map(int,input().split()))
X = list(map(int,input().split()))
solve(N,M,S,X)
