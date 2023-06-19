# 리스트에 1~30 넣기 -> for문으로 입력받는 28개 숫자 리스트에서 지우기
# -> min , max 출력
arr_list = [i for i in range(1,31)]

for j in range(28):
    x = int(input())
    arr_list.remove(x)
    
print(min(arr_list))
print(max(arr_list))
    
