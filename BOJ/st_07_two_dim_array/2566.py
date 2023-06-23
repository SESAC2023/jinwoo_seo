import sys
input = sys.stdin.readline

arr_list = []

for i in range(9):
    arr_list.append(list(map(int, input().split())))
    
x = 0
y = 0
max = -1

for i in range(9):
    for j in range(9):
        if arr_list[i][j] > max:
            max = arr_list[i][j]
            x = i+1
            y = j+1
print(max)
print(x, y)
