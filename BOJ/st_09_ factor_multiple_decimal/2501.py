"""
1부터 n까지 수를 올려가며 n을 나눈다.
만약 나누어 떨어질 경우 k를 하나씩 감소시킨다.
k가 0이 된다면, 현재 수가 k번째 작은 약수이므로 현재 수를 출력하고 break 한다.
k가 0이 되기전에 반복문이 끝난다면 약수의 개수가 k개 보다 적다는 의미이므로 0을 출력한다.
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

for i in range(1,N+1):
    if N % i == 0:
        K -= 1
    if K == 0:
        print(i)
        break
else:
    print(0)
