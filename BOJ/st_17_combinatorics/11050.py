# n! / k!(n-k!)

import sys
input = sys.stdin.readline
# for문
def factorial(n):
    if n == 0:
        return 1
      
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))

# 재귀문
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))
