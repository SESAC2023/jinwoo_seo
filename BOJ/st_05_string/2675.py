T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    
    for j in S:
        print(R * j, end = "") # end ="" 공백없이 출력
    print() # 한줄 넘겨서 출력
