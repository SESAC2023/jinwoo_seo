# 작은 두 변의 길이의 합이 제일 긴 변의 길이보다 커야 된다는 점을 사용하면 쉽게 풀 수 있다.

arr = sorted(map(int, input().split()))
result = arr[0] + arr[1] + min(arr[2], arr[0]+arr[1]-1)
print(result)
