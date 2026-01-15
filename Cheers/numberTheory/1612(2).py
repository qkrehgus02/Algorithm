#기존 1612 코드에서 조금 더 간결하게 코드를 정리하였습니다. 

n = int(input())
ans = -1

if n % 2 != 0 and n % 5 != 0:
    length = len(str(n))
    
    if length == 1:
        k2 = 0
    else:
        k2 = int("1" * (length - 1))
        
    k = int("1" * length)

    while True:
        if k % n == 0:
            ans = length
            break
        elif k % n == k2:
            break
        else:
            k = (k % n) * 10 + 1
            length += 1

print(ans)