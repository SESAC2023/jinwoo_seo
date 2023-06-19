# arr_list = arr_list[:a-1] + arr_list[a-1:b][::-1] + arr_list[:b]
# ==
# arr_list[a-1:b] = reversed(arr_list[a-1:b])

x, y = map(int, input().split())
arr_list = [i for i in range(1, x+1)]

for j in range(y):
    a,b = map(int, input().split())
    arr_list[a-1:b] = reversed(arr_list[a-1:b])

for k in range(x):
    print(arr_list[k], end = " ")
