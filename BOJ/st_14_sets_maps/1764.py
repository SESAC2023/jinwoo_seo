import sys
input = sys.stdin.readline

n,m = map(int, input().split())

a = set()

for i in range(n):
    a.add(input().strip())

b = set()
for i in range(m):
    b.add(input().strip())

result = sorted(list(a & b))

print(len(result))

for i in result:
    print(i)
