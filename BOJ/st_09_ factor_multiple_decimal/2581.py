import sys
input = sys.stdin.readline

M = int(input())
N = int(input())

sosu = []
for num in range(M, N+1):
    cnt = 0
    if num > 1:
        for i in range(2, num): # 2부터 num-1까지
            if num % i == 0:
                cnt += 1
                break # 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
        if cnt == 0:
            sosu.append(num) # error가 없으면 소수리스트에 추가
if len(sosu) > 0:
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)
