def factorize(n) :
    factors = []

    for i in range(2,int(n ** 0.5)) :
        while n % i == 0 :
            factors.append(i)
            n //= i
    if n != 1 :
        factors.append(n)
    
    return factors

n = int(input())
factor = factorize(n)
print(" ".join(map(str,factor)))

