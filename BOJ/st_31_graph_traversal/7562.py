import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
from collections import deque


tc = int(input()) 

for _ in range(tc):
    n = int(input())
    now = list(map(int, sys.input().split()))
    dest = list(map(int, sys.input().split()))   

    matrix = [[0]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]

    q = deque()
    
    # 시계방향
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]


    def bfs():
        q.append(now)
        visited[now[0]][now[1]]

        while q:
            x, y = q.popleft()

            if x == dest[0] and y == dest[1] :
                return 0

            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]

                if nx <0 or nx>=n or ny<0 or ny>=n:
                    continue

                if nx == dest[0] and ny == dest[1]:
                    visited[nx][ny] = True
                    return matrix[x][y]+1

                if visited[nx][ny] == False:
                    q.append([nx,ny])
                    visited[nx][ny] = True
                    matrix[nx][ny] = matrix[x][y] + 1    
    
    answer = bfs()
    print(answer)
