#앞자리가 클수록 우선순위
#두번째자리부터 다음과 같은 우선순위로 정렬
#ab -> a -> ac (c < a < b)

from collections import defaultdict

N = int(input())
num = list(map(int, input().split()))

def sorting(numlist, check, standard):
    if len(numlist) <= 1:
        return numlist

    groups = defaultdict(list)
    mid = []

    for n in numlist:
        if len(str(n)) <= check:
            mid.append(n)
        else:
            groups[str(n)[check]].append(n)

    result = []
    for i in range(9, -1, -1):
        if str(i) in groups:
            result += sorting(groups[str(i)], check+1, str(i))
        if str(i) == standard:
            result += mid

    return result

result = sorting(num, 0, '')
answer = int(''.join(map(str, result)))
print(answer)