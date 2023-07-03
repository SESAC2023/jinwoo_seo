import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
from collections import deque
MAX = 50 + 10

n, k = map(int, input().split())

def bfs(a,b):
    q = []
    visited = [False] * 200001
    
    q.append(a)
    visited[a] = 1
    
    while q:
        x = q.popleft()
        if x == b:
            return visited[b]-1
        for i in (x-1, x+1, x*2):
            if 0 <= i <= 200000 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[x] + 1
                
    return -1
print(bfs(n,k))
