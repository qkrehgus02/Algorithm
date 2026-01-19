n, m = map(int, input().split())

def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

print(m - gcd(n, m))