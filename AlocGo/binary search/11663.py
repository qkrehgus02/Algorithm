n, m = map(int,input().split())

dot = list(map(int, input().split()))

dot.sort()

def binary1(array, target, left, right):
    position = right + 1
    
    while left <= right:
        mid = (left + right) // 2

        if array[mid] >= target:
            right = mid - 1
            position = mid
        else:
            left = mid + 1 
    return position
#자기자신의 위치거나 자기보다 작은 위치를 출력하도록 만든 함수. 

def binary2(array, target, left, right):
    position = right + 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] > target:
            right = mid - 1
            position = mid
        else:
            left = mid + 1 
    return position

result = []

for _ in range(m):
    a, b = map(int, input().split())
    
    l = binary1(dot, a, 0, n - 1)
    r = binary2(dot, b, 0, n - 1)
    result.append(r-l)
    
for r in result:
    print(r)    