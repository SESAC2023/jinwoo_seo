# num을 2부터 √num 까지 나누어서 구하는 알고리즘(num의 약수의 중간을 구하는 원리) => 시간복잡도 O(√n)
import sys
import math

def is_prime(num):
  if num == 0 or num == 1:
    return False
  else:
    for i in range(2, int(math.sqrt(num)) + 1):
      if num % i == 0:
        return False
    return num

def next_num(num):
  while True:
    if is_prime(num) == False:
      num += 1
    elif is_prime(num):
      return num

input = sys.stdin.readline

n = int(input())

for _ in range(n):
  num = int(input())
  print(next_num(num))
