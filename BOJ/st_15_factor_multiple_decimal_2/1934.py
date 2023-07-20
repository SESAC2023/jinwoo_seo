import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    X, Y = x, y
    while x != 0:
        y = y % x
        x, y = y, x
        
    gcd = y
    lcm = X * Y // y
    print(lcm)
