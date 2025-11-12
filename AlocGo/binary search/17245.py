n = int(input())

server_room = []

for _ in range(n):
    server_room += list(map(int, input().split()))

left = 0
right = max(server_room)
total = sum(server_room)
ans = 0 

while left <= right:
    mid = (left + right) // 2
    
    sum = 0
    
    for c in server_room:
        if c >= mid:
            sum += mid
        else:
            sum += c
    
    if sum < total / 2:
        left = mid + 1
    else:
        right = mid - 1
        ans = mid

print(ans)