arr_list = []
for i in range(9):
    arr_list.append(int(input()))

print(max(arr_list))
print(arr_list.index(max(arr_list))+1)
