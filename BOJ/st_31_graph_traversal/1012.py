import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
from collections import deque
MAX = 50 + 10

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(y, x):
    global visited
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if graph[ny][nx] and not visited[ny][nx]:
            dfs(ny, nx)
    

t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split())
    graph = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y + 1][x + 1] = True
        
    answer = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                answer += 1
    
    print(answer)
