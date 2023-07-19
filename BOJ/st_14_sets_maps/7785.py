import sys
input = sys.stdin.readline

n = int(input())
temp = {}

for i in range(n):
    a, b = map(str, input().split())
    
    if b == 'enter':
        temp[a] = b
    else:
        del temp[a]
        
temp = sorted(temp.keys(), reverse = True)

for j in temp:
    print(j)
