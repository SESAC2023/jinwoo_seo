# 1번 정답
import sys
input = sys.stdin.readline

s = input()

for i in s:
    if i.isupper():
         print(i.lower(), end='')
    else:
         print(i.upper(), end='')

====================================================
# 2번 정답
print(input().swapcase())
