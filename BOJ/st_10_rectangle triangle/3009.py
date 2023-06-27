"""
말 그대로 직사각형의 나머지 한 좌표를 찾는 문제이다.
단순히 x값으로 주어지는 3 좌표, y값으로 주어지는 3 좌표 중
짝이 없는 하나의 좌표를 찾아 출력하면 되었다.
"""

import sys
input = sys.stdin.readline

def d(n):	# x, y 두 번 반복해야 하므로 함수를 활용하여 코드를 줄였다.
    if n[0] == n[1]:
        return n[2]
    elif n[0] == n[2]:
        return n[1]
    else:
        return n[0]

x,y = [],[]
for i in range(3):
    a,b = map(int,input().split())
    x.append(a); y.append(b)
print(d(x),d(y))
