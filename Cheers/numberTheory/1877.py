m = int(input())

def factorization(n):
    factors = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    if n > 1 : 
        factors.append(n)
    
    return factors

def quizA(M):
    max = 0
    min = 0
    
    n = M // 3
    if M % 3 == 0:
        max = n
        min = n
    elif M % 3 == 1 : 
        max = n + 1
        min = n
    else: 
        max = n + 1
        min = n + 1
    
    return max, min

def quizB(M):
    factors = factorization(M)
    max = len(factors)
    count = 0
    for f in factors:
        if f == 2: #2의 개수를 셈. 
            count += 1
    count = count // 2
    min = max - count
    
    return max, min

if m != 1:
    a1, a2 = quizA(m)
    a3, a4 = quizB(m)

    print(a1, a2, a3, a4)
else:
    print(1, 1, 1, 1)