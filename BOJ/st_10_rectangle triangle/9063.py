import sys
input = sys.stdin.readline

N = int(input())

x, y = [],[]
for i in range(N):
    a, b = map(int, input().split())
    x.append(a); y.append(b)
print((max(x)-min(x)) * (max(y) - min(y)))
