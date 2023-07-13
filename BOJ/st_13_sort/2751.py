import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())
list = []
for i in range(n):
    list.append(int(input()))
for i in sorted(list):
    print(i)
