k = int(input())

a = 1
start = 0
end = 0
result = 2 # 2부터 시작

while a <= 2000000:
    if k == a:
        start = a
        end = a
        break
    elif k < a:
        end = a
        break
    start = a  # k보다 작은 2의 제곱수 저장
    a *= 2

if(start == end): #둘이 같으면 k는 제곱수
    print(start, 0) #초콜릿을 쪼개지 않아도 되고, 크기는 자기자신과 같음. 
else:
    chocolate = end
    while True:
        mid = (start + end) // 2  # 정수 나누기로 변경
        if mid == k : #우리가 찾고자하는 값이면
            break

        if mid > k : #우리가 찾고싶은 값이 더 작으면
            end = mid
            result += 1
        elif mid < k : #우리가 찾고싶은 값이 더 크면
            start = mid
            result += 1

    print(chocolate, result)
        