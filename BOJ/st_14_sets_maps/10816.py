import sys
from collections import Counter
input = sys.stdin.readline

M = int(input())
list1 = list(map(int,input().split()))
N = int(input())
list2 = list(map(int,input().split()))

c = Counter(list1)

for i in list2:
  if i in c:
    print(c[i], end=' ')
  else:
    print(0, end=' ')
