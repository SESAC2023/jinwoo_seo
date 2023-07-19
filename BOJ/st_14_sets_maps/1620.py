import sys
input = sys.stdin.readline

n, m = map(int, input().split())

temp = {}

for i in range(1, n+1):
    a = input().strip()
    temp[i] = a
    temp[a] = i
    
for i in range(m):
    b = input().strip()
    if b.isdigit():
        print(temp[int(b)])
    else:
        print(temp[b])
