n = int(input())
 
arr = [] # 2차원리스트
for _ in range(n):
    x = list(map(int,input().split()))
    arr.append([x[1],x[0]])
 
arr.sort()
 
for i in arr:
    print(i[1],i[0])
