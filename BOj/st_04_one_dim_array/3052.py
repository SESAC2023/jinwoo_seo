# set으로 중복 값 제거 -> len으로 몇개인지 알아내기

arr_list = []

for i in range(10):
    x = int(input())
    arr_list.append(x % 42)

arr_list = set(arr_list)
print(len(arr_list))
