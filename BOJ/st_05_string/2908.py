# 들어오는 숫자를 str타입으로 받아서 역순 처리
x,y = map(str, input().split())

x = x[::-1]
y = y[::-1]

print(int(max(x,y)))
