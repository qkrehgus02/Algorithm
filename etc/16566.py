#sol 1 - 이분탐색을 이용한 접근, 시간 초과
#list.pop()에서 시간초과가 난 것으로 보임. union-find를 활용해야할 것 같다. 

#n, m, k = map(int, input().split())
#
#m_list = list(map(int, input().split()))
#k_list = list(map(int, input().split()))
#
#result = []
#
#m_list.sort()
#
#def binary_search(left, right, key, list):
#    mid = (left + right) // 2
#    
#    if list[mid] == key:
#        return mid + 1
#    elif left == mid:
#        return mid
#    
#    else:
#        if list[mid] < key:
#            return binary_search(mid, right, key, list)
#        elif list[mid] > key:
#            return binary_search(left, mid, key, list)
#
#for key in k_list:
#    target = binary_search(0, len(m_list)-1, key, m_list)
#    result.append(m_list[target])
#    
#    m_list.pop(target)
#
#for r in result:
#    print(r)


n, m, k = map(int, input().split())

m_list = list(map(int, input().split()))
k_list = list(map(int, input().split()))

parent = [i for i in range(m+1)]

result = []

m_list.sort()

def binary_search(left, right, key, list):
    mid = (left + right) // 2
    
    if list[mid] == key:
        return mid + 1
    elif left == mid:
        if list[mid] < key:
            return mid + 1
        return mid 
    
    else:
        if list[mid] < key:
            return binary_search(mid, right, key, list)
        elif list[mid] > key:
            return binary_search(left, mid, key, list)

def find(i):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i])
    return parent[i]

for key in k_list:
    target = binary_search(0, len(m_list)-1, key, m_list)
    actual = find(target)
    result.append(m_list[actual])
    
    parent[actual] = find(actual + 1)

for r in result:
    print(r)