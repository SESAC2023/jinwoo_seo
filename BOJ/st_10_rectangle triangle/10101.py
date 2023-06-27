import sys
input = sys.stdin.readline

al = [int(input()) for _ in range(3)]

if sum(al) != 180:
    print("Error")
elif al[0] == al[1] == al[2]:
    print("Equilateral")
elif al[0] != al[1] and al[0] != al[2] and al[1] != al[2]:
    print("Scalene")
else:
    print("Isosceles")
