import sys
input = sys.stdin.readline

T = int(input())
coin = [25,10,5,1] #큰 거스름돈 부터 먼저 나눠준다.

for i in range(T):
    C = int(input())
    result=[]
    
    for j in range(4):
        result.append(C // coin[j]) # C를 coin 인덱스 번호 순서대로 나눈 몫을 차례대로 넣어준다.
        C = C % coin[j] # 앞 인덱스 번호의 코인이 나누고 남은 값이 C에 들어가게 해준다.
    print(*result) # print(*) 한 줄 출력
