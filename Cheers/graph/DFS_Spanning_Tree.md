# DFS 스패닝 트리

## 개념

그래프에서 DFS를 수행할 때, **방문에 사용된 간선들**만 모으면 트리가 된다. 이것이 DFS 스패닝 트리.

## 간선의 분류

| 간선 종류 | 설명 |
|-----------|------|
| 트리 간선 (Tree Edge) | DFS 트리에 포함된 간선 |
| 역방향 간선 (Back Edge) | 자손 → 조상으로 향하는 간선 |
| 순방향 간선 (Forward Edge) | 조상 → 자손 (트리 간선 제외, 방향 그래프에서만) |
| 교차 간선 (Cross Edge) | 나머지 (방향 그래프에서만) |

> 무방향 그래프에서는 **트리 간선**과 **역방향 간선**만 존재

---

## disc와 low

### disc (discovery time)
- DFS에서 해당 정점을 **처음 방문한 순서**

### low
- 해당 정점에서 **자손들과 역방향 간선을 통해 도달할 수 있는 가장 작은 disc 값**
- 즉, "내 subtree 전체가 도달할 수 있는 가장 높은 곳"

```
low[node] = min(
    disc[node],                     # 자기 자신
    disc[x]   (역방향 간선으로 연결된 조상 x),
    low[child] (트리 간선으로 연결된 자식 child)
)
```

### 계산 방식
- DFS 재귀가 돌아오면서(return 할 때) 자식의 low 값이 부모로 **전파**됨

---

## 단절점 (Articulation Point)

### 조건: `low[child] >= disc[node]`

**의미**: 자식 subtree에서 역방향 간선을 아무리 타도, node보다 위로 못 올라감
→ node를 제거하면 자식 subtree가 고립 → **단절점**

### 루트 예외
- 루트는 위 조건 대신, **DFS 트리에서 자식이 2개 이상**이면 단절점

### 주의
- 같은 노드가 여러 자식 때문에 조건을 만족할 수 있으므로 `is_cut[]` 배열로 중복 방지

---

## 단절선 (Bridge)

### 조건: `low[child] > disc[node]`

**의미**: 자식 subtree에서 역방향 간선을 타도, node까지도 못 올라감
→ (node, child) 간선을 끊으면 분리 → **단절선**

### 단절점과의 차이 (`>=` vs `>`)

```
low[child] == disc[node] 일 때:
- 우회로로 node까지는 돌아올 수 있음
- node 자체를 없애면 우회로도 사라짐 → 단절점 O
- 간선만 끊으면 우회로로 연결 유지    → 단절선 X
```

> 단절선 = 어떤 사이클에도 속하지 않는 간선

---

## 구현 코드 (단절점)

```python
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)
disc = [0] * (v+1)
low = [0] * (v+1)
is_cut = [False] * (v+1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

order = 0

def dfs(node, parent):
    global order
    order += 1
    disc[node] = low[node] = order
    child_count = 0

    for child in graph[node]:
        if not visited[child]:          # 트리 간선
            visited[child] = True
            child_count += 1
            dfs(child, node)
            low[node] = min(low[node], low[child])

            # 루트가 아닌 경우
            if parent != 0 and low[child] >= disc[node]:
                is_cut[node] = True
        elif child != parent:           # 역방향 간선
            low[node] = min(low[node], disc[child])

    # 루트인 경우: DFS 트리 자식이 2개 이상이면 단절점
    if parent == 0 and child_count >= 2:
        is_cut[node] = True

# 비연결 그래프 대응: 모든 정점에서 DFS
for i in range(1, v+1):
    if not visited[i]:
        visited[i] = True
        dfs(i, 0)

anslist = [i for i in range(1, v+1) if is_cut[i]]
print(len(anslist))
print(*anslist)
```

### 핵심 포인트 정리
1. **low 값은 재귀적으로** 계산 (자식 return 후 전파)
2. **단절점 판별은 DFS 안에서** (자식 재귀 끝난 직후)
3. **루트는 예외** 처리 (자식 수로 판별)
4. **is_cut 배열**로 중복 방지
5. **비연결 그래프**면 모든 정점에서 DFS 시작
