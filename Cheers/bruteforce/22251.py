N, K, P, X = map(int, input().split())
# N - 건물의 층수
# K - 디스플레이의 개수
# P - 반전시킬 디스플레이 개수
# X - 실제로 멈춰있는 층

#각 디스플레이를 표현
display = [[] for _ in range(10)]
display[0] = [1, 1, 1, 0, 1, 1, 1]
display[1] = [0, 0, 1, 0, 0, 1, 0]
display[2] = [1, 0, 1, 1, 1, 0, 1]
display[3] = [1, 0, 1, 1, 0, 1, 1]
display[4] = [0, 1, 1, 1, 0, 1, 0]
display[5] = [1, 1, 0, 1, 0, 1, 1]
display[6] = [1, 1, 0, 1, 1, 1, 1]
display[7] = [1, 0, 1, 0, 0, 1, 0]
display[8] = [1, 1, 1, 1, 1, 1, 1]
display[9] = [1, 1, 1, 1, 0, 1, 1]

def countReverse(a, b):
    count = 0
    for i in range(7):
        if display[a][i] != display[b][i]:
            count += 1
    return count
    
#디스플레이끼리 바뀌는 배열을 표현
reverse = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(i + 1, 10):  # j > i 일 때만 계산
        count = countReverse(i, j)
        reverse[i][j] = count
        reverse[j][i] = count  # 대칭으로 저장
        
X_list = [0 for _ in range(K)]  
num_list = [0 for _ in range(K)]
  
for i in range(K):
    X_list[i] = X%10
    X = X//10

result = 0

for i in range(1, N+1):
    count = 0
    for j in range(K):
        num_list[j] = i%10
        i = i//10
    for i in range(K):
        count += reverse[X_list[i]][num_list[i]]
    if count <= P:
        result += 1

print(result-1) #자기자신으로 바뀌는 경우 하나 빼기