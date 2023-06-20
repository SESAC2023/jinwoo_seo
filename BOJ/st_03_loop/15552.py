import sys

x = int(sys.stdin.readline().rstrip())

for i in range(x):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
