# 벌집이 6의 배수로 증가
N = int(input())

bulzip = 1
total_cnt = 1

while N > bulzip:
    bulzip += 6 * total_cnt
    total_cnt += 1
print(total_cnt)
