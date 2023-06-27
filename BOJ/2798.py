import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in combinations(arr, 3):
    total_sum = sum(i)
    if result < total_sum and total_sum <= M:
        result = total_sum
print(result) 
