import sys

input = sys.stdin.readline

n = int(input())
card_list = list(map(int, input().split()))
m = int(input())
check_list = list(map(int, input().split()))
result = []

card_list.sort()

def binary_search(array, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == target:
            return True
        elif array[mid] > target:
            right = mid -1 
        else:
            left = mid + 1
    return False

for c in check_list:
    if binary_search(card_list, c, 0, n - 1):
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))