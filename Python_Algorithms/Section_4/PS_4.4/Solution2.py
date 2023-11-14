def fatorize(n,m) :
    if n < 2 :
        return []
    elif m > int(n ** 0.5) :
        return [n]
    elif n % m == 0 :
        return [m] + fatorize(n // m,m)
    else:
        return fatorize(n,m + 1)
    
n,m = map(int,input().split())

print(fatorize(n,m))