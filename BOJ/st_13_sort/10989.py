import sys

N  = int(sys.stdin.readline())
arr = [0]*10001

for _ in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1 # arr[num]에 num이 들어온 개수 count 

for i in range(10001): 
	# arr[i]에 숫자가 들어왔다면 
    if arr[i] != 0:
    	# `arr[i]`번 반복합니다. 이 반복문은 `i` 숫자가 등장한 횟수만큼 반복하게 됩니다. 
        for j in range(arr[i]): 
            print(i)