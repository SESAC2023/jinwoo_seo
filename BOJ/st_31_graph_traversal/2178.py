import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
from collections import deque
MAX = 50 + 10

n,m = map(int, input().split())
graph = []
for _ in range(n):
    line = input().strip()
    current = []
    for x in line:
        current.append(int(x))
    graph.append(current)
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    q = deque()
    q.append([a,b])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx,ny])
    return graph[n-1][m-1]
print(bfs(0,0))
