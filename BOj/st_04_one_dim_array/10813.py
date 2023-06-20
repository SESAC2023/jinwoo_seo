# baguni 리스트에 1~N 숫자 넣기 -> [i for i in range(1, N+1)]
# 변수 서로 바꾸기 -> baguni[i-1], baguni[j-1] = baguni[j-1], baguni[i-1]
# 다른 언어에선 tmp = 0 / tmp = baguni[i-1]/ baguni[i-1] = baguni[j-1]
# / baguni[j-1] = tmp

N, M = map(int, input().split())
baguni = [i for i in range(1, N+1)]

for y in range(M):
    i, j = map(int, input().split())
    baguni[i-1], baguni[j-1] = baguni[j-1], baguni[i-1]
   
    
for z in range(N):
    print(baguni[z], end=" ")
