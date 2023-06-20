x = list(str(input()))
arr_list = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

total_time = 0

for i in x:
    for j in arr_list:
        if i in j:
            total_time += arr_list.index(j) +3

print(total_time)
