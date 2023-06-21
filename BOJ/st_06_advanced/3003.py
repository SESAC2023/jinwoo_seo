x = list(map(int, input().split()))

arr_list = [1,1,2,2,2,8] 

for i in range(len(arr_list)):
    print(arr_list[i] - x[i], end = " ")
