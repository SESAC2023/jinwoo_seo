# 시(hour)는 60을 나눈 몫 , 분(m)은 60을 나눈 나머지로 구할 수 있다. 그리고 if문으로 24시가 넘으면 0으로 바꿔주고(h=h-24) 분은 60분이 넘으면
# 0분으로 바꿔주고  hour를 1 올린다.(m=m-60, h+=1)

h, m = map(int, input().split())
t = int(input()) 

h += t // 60 
m += t % 60

if h >= 24:
    h -= 24

if m >= 60:
    h += 1
    m -= 60

print(h, m)
