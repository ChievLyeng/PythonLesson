def factorize(n) :
    if n < 2 :
        return []
    else:
        for i in range(2,int(n ** 0.5) + 1) :
            if n % i == 0 :
                # print("Prime :",[i] + factorize(n // i))
                return [i] + factorize(n // i)
        return [n]
    
n = int(input())
factors = factorize(n)
print("Prime fatorize :"," ".join(map(str,factors)))
        