import sys
input = sys.stdin.readline

n = int(input())
x = 1

if n >0:
    for i in range(1, n+1):
        x = x*i
print(x)
