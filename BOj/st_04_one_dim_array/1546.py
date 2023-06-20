N = int(input())
arr_list = list(map(int, input().split()))
max_list = max(arr_list)

result_list=[]
for i in arr_list: # range xxx!! 주의!
    result_list.append(i/max_list*100)

result = sum(result_list)/N
print(result)
