"""
최대 100개 이하의 1000 이하 자연수가 주어진다.
성능을 크게 요하지 않는 문제이므로, 최적화는 신경 쓰지 않았다.
소수는 2 이상의 숫자 중 자신과 1 만을 약수로 두는 수를 의미한다.
따라서, N을 소수로 판별하는 법은 N을 (여기서 N은 N>1) 2 ~ N-1 로 차례로 나눌 때
한 번도 나누어지지 않는다면 소수라고 판별할 수 있다.
"""

import sys
input = sys.stdin.readline

x = int(input())
y = list(map(int, input().split()))
cnt = 0

for i in range(x):
    if y[i] < 2:
        continue
    for j in range(2, y[i]):
        if y[i] % j == 0:
            break
    else:
        cnt += 1
print(cnt)
