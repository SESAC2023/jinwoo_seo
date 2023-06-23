import sys
input = sys.stdin.readline

array_list = [[0 for _ in range(101)]for _ in range(101)]
N = int(input())

for i in range(N):
    x, y = list(map(int, input().split()))
    
    for row in range(x, x+10):
        for col in range(y, y+10):
            array_list[row][col] = 1
         
result = 0

for i in array_list:
    result += i.count(1)
print(result)
