from collections import deque

n, k = map(int, input().split())

INF = 1000000
cost = [INF for _ in range(100001)]
cost[n] = 0

deq = deque()
deq.append((n, 0))

while deq:
    position, weight = deq.popleft()
    
    if position == k:
        print(weight)
        break
    
    np = position * 2
    if 0 <= np <=100000 and cost[np] > weight:
        cost[np] = weight
        deq.appendleft((np, weight))
        
    np = position + 1
    if 0 <= np <= 100000 and cost[np] > weight + 1:
        cost[np] = weight + 1
        deq.append((np, weight + 1))
        
    np = position - 1   
    if 0 <= np <= 100000 and cost[np] > weight + 1:
        cost[np] = weight + 1
        deq.append((np, weight + 1))

