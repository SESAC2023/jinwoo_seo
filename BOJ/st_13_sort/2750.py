import sys
input = sys.stdin.readline

x = int(input())
num_list = []
for i in range(x):
    num_list.append(int(input()))
result= sorted(num_list)
for i in range(len(num_list)):
    print(result[i])
    
