N,X = map(int, input().split())

arr_list = list(map(int, input().split()))

for i in range(N):
    if arr_list[i] < X:
        print(arr_list[i], end=" ")
