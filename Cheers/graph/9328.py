h, w = map(int, input().split())
graph = []

for _ in range(h):
    graph.append(list(input()))

#그래프를 전체 탐색하면서 $를 만나면 그래프에 방문 처리
#소문자를 만나면 열쇠 리스트에 넣고 방문 처리
#대문자를 만나도 방문처리

#한

print(graph) 