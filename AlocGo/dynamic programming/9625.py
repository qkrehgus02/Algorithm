k = int(input())

b = [0 for _ in range(k+1)]
b[0] = 0
b[1] = 1

if k>= 2:
    b[2] = 1

if k >= 3:
    for i in range(3, k+1):
        b[i] = b[i-1] + b[i-2]
        
        
print(b[k-1], b[k])