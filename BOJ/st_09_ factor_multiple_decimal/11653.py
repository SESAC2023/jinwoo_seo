"""
주어진 N이 2 이상일 때, 2부터 나누어 나누어 떨어지는 수를 출력한다.
그리고 나누어주는 수를 다시 2로 초기화하여 계산한다.
최적화는 고려하지 않았다.
만약 고려해야 할 경우, 가장 마지막으로 분해한 소인수보다 작은 수는
반복에서 제외하는 등의 방법을 활용할 수 있겠다.
"""
import sys
input = sys.stdin.readline

N = int(input())
bunhae = 2
while (N>1):
    if N % bunhae == 0:
        print(bunhae)
        N = N / bunhae
    
    else:
        bunhae += 1
