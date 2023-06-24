"""
<24479>
1. 내용 훑기 - 그래프, DFS, 방문처리, 탐색
2.(중요) 입력 조건:
-노드(도시) 혹은 정점 개수 최대 100,000개
-간선(도로) 개수 최대 200,000개
3. 문제 아이디어 생각하기
DFS로 풀면 되지 않을까?
DFS가 시간 복잡도가 O(M+N)이니까, 단순 DFS로도 가능
"""

import sys
# 재귀 깊이 한도 해제
sys.setrecursionlimit(int(1e6))
# 빠르게 입력받기
input = sys.stdin.readline

# n(노드개수), m(간선개수), r(시작노드)
n, m, r = map(int, input().split())
"""
graph = [
    [],
    [2, 4],
    [1, 3, 4],
    [2, 4],
    [1, 2, 3],
    []
]
"""
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
answer = [0] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    # graph[u].append(v) / graph[v].append(u) -> 무방향 그래프 = 양방향 그래프 , 방향이 한쪽이면 graph[u].append(v) 만 하면 됨.
    graph[u].append(v)
    graph[v].append(u)

cnt = 1

# 전형적인 DFS 코드
def dfs(x):
    global cnt
    visited[x] = True # 현재 노드 방문 처리
    answer[x] = cnt # 방문한 순서 기록
    cnt += 1
    # 현재 노드와 인접한 노드 중에서
    for y in graph[x]:
        # 방문하지 않은 노드가 있다면 재귀 호출
        if not visited[y]:
            dfs(y)


# 인접한 노드를 오름차순으로 방문하기 위해 정렬
for i in range(1, n + 1):
    graph[i].sort()

# DFS 수행
dfs(r)

# 각 노드에 대하여 방문한 순서 출력
for i in range(1, n + 1):
    print(answer[i])
