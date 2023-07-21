import sys
input = sys.stdin.readline
import math

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

x = a1 * b2 + a2 * b1 #분자
y = b1 * b2 # 분모

gcd = math.gcd(x, y)
x //= gcd
y //= gcd

print(x, y)
