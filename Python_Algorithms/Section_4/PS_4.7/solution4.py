def solve(n) :
    cnt = 0
    for c  in range( (n + 1) // 3, (n + 1) // 2 ) :
        cnt += c - (n - c + 1) // 2 + 1
    return cnt

n = int(input())
print(solve(n))