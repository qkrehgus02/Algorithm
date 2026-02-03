A, B = map(int, input().split())

#BFS를 이용
#목표값보다 작은 값이라면?
#2를 곱한값, 1을 추가한 값을 큐에 넣음
#중복되는 경우는 없는게 전자는 짝수, 후자는 홀수이기 때문에 방문처리는 딱히 안해도 된다. 
#큐에 값이 다 빠져나갈때까지 답을 못찾으면 답이 없는것. 

from collections import deque


def bfs(start):
    queue = deque()
    queue.append((start, 0))

    while queue:
        num, count = queue.popleft()
        if num < B: #B보다 작다면
            if num * 10 + 1 == B: 
                return count + 2
            elif num * 2 == B:
                return count + 2
            else: #만약 답을 못 찾았으면
                queue.append((num*10 + 1, count + 1))
                queue.append((num*2, count+1))
    
    return -1

print(bfs(A))
            
