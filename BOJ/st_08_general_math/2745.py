# 파이썬의 경우 int 함수를 활용하여 간단하게 n진법을 10진법으로 변환할 수 있다.
# int(변환할string, n진법) 형식으로 사용한다.n진법은 int형으로 입력해야 한다.
a, b = input().rstrip().split()
print(int(a, int(b)))
