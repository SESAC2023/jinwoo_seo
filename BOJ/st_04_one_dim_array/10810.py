# 1. baguni 라는 리스트 생성하고 값 0으로 초기화 해줌 -> 
# 공이 없는 바구니는 0을 출력해야 하기 때문에
# 2. M번 for문 -> i바구니부터 j바구니 까지 포함해야 하므로 j+1
# i~j바구니 까지 k번호 공 넣는데 인덱스는 0부터 시작하므로 
# baguni[x-1] = k
# 3. for 문 나와서 모든 N개의 바구니에 어떤 k 번호의 공이 들어있는지
# 출력하기 위해 for문 / baguni[y] 로 baguni 리스트에 들어있는 값
# 순서대로 출

N,M = map(int, input().split())
baguni = [0 for _ in range(N)]

for _ in range(M):
    i,j,k = map(int, input().split())
    for x in range(i, j+1):
        baguni[x-1] = k

for y in range(N):
    print(baguni[y], end=" ")
