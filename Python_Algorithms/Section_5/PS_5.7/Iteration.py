def cut(n,s,h) :
    a = list(s[i] - h for i in range(n) if s[i] > h)
    print(a,end=" ")
    print(sum(a))
    return sum(s[i] - h for i in range(n) if s[i] > h)

    # length = 0
    # for i in range(n) :
    #     if s[i] > h :
    #         length += s[i] - h
    # return length
    
def binsearch(n,M,s) :
    low,high = 0, max(s)
    cnt = 0
    while low < high :
        cnt += 1
        mid = (low + high) // 2
        if cut(n,s,mid) < M :
            high = mid
        else :
            low = mid + 1
    print("cnt :",cnt,"low :",low)
    return low - 1

def solve(n,M,s) :
    j = binsearch(n,M,s)
    print(j)

N,M = map(int,input().split())
S = list(map(int,input().split()))
solve(N,M,S)