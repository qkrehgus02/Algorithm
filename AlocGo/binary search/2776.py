t = int(input())

for i in range(t):

    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    note1.sort()

    def binary_search(array, target, left, right):
        while left <= right:
            mid = (left + right) // 2

            if array[mid] == target:
                return 1
            elif array[mid] > target:
                right = mid - 1
            else: 
                left = mid + 1
        return 0

    result = []

    for n2 in note2:
        result.append(binary_search(note1, n2, 0, n - 1))

    for r in result:
        print(r)