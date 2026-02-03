#X원을 거슬러주어야 한다. 500, 100, 50, 10원짜리 동전이 무한정 있을 때, 최대한 적은 개수의 동전으로 거스름돈을 거슬러주는 경우를 구하시오. 

X = int(input())

coins = [500, 100, 50, 10]
count = 0
result = {}

# 1. 선택 절차 적용 : 거스름돈 문제에서 가장 가치가 큰 동전부터 선택
coins.sort(reverse=True)

#2. 적절성 검사 : 선택된 동전의 가치가 거스름돈보다 크다면 다음으로 작은 동전을 선택
for coin in coins:
    result[str(coin)] = X // coin
    X %= coin 

#3. 해답 검사 : 최종적으로 원하는 값과 일치하는지 검사. 
if X == 0:
    print(result)
    
    
    
    
    