def binsearch(x,n,s) :
    low,high = 0,n - 1 # search range (from low to high)
    cnt = 0
    while low <= high :
        cnt += 1
        # print(low,high)
        mid = (low + high) // 2
        # print("mid :",mid)
        # print("s[mid] :",s[mid])
        if x == s[mid] :
            return mid,cnt # mid is the index of search element
        elif x < s[mid] :
            high = mid - 1
        else : #x > s[mid] 
            low = mid + 1
    return -1

def solve(N,M,S,X) :
    for i in range(M) :
        j,count= binsearch(X[i],N,S)
        # print("searched Index :",j)
        # print("Iteration :",count)
        print(j,end=" ")


N,M = map(int,input().split())
S = list(map(int,input().split()))
X = list(map(int,input().split()))
solve(N,M,S,X)
