# try except 활용
while True:
    try:
        x,y = map(int, input().split())
        print(x+y)
    except:
        break
