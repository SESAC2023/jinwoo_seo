total_price = int(input())
total_num = int(input())

sum = 0

for i in range(total_num):
    price, num = map(int, input().split())       
    
    sum = sum + price * num
    
if sum == total_price:
    print("Yes")
else:
    print("No")
