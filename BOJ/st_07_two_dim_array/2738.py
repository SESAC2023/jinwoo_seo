import sys
input = sys.stdin.readline

N, M = map(int, input().split())

x = [[0 for i in range(M)] for j in range(N)]
y = [[0 for i in range(M)] for j in range(N)]

for i in range(0, N):
	x[i] = list(map(int, input().split())) 

for i in range(0, N):
	y[i] = list(map(int, input().split()))

for i in range(0, N):
	for j in range(0, M):
		x[i][j] += y[i][j]
		print(x[i][j], end = " ")
	print()
