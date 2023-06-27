"""
직사각형 안 좌표에서 최단 거리를 찾는 문제이다.
경계선까지의 거리는 항상 직선 거리가 최단이기 때문에,
굳이 대각선으로 이동할 필요가 없으므로
좌표에서 4방향 직선거리 중 가장 짧은 것을 출력하면 된다.
"""

import sys
input = sys.stdin.readline

x,y,w,h = map(int, input().split())

print(min(x, y, w-x, h-y))
