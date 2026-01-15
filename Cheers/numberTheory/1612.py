n = int(input())

if n == 1:
    print(1)
elif n == 3:
    print(3)
elif n == 7:
    print(6)
elif n == 9: 
    print(9)
else:
    ans = -1

    if n % 2 != 0  and n % 5 != 0: 
        length = int(len(str(n))) #우선 자릿수 구하고
        n = int(n)
        k =  int("1" * length)
        k2 = int("1" * (length - 1))

        while True:
            if k % n == 0: #만약 나누어떨어지면
                ans = length
                break #종료
            elif k % n == k2 : #만약 나눈 결과가 k2이면 1로 이루어진 수를 만들 수 없음. 
                break #종료 -> -1이 출력될 것
            else: # 두가지 조건에 모두 맞지 않는다면?
                k = (k % n) * 10 + 1
                length += 1
        print(ans)
    else : 
        print(ans)