import sys
input = sys.stdin.readline

a, b = map(int, input().split())
mul = a*b

#최대공약수(유클리드 호제법)
while b:
    if a > b:
        a, b = b, a
    b = b % a
print(mul // a)
