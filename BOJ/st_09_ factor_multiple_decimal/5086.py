import sys
sys.stdin.readline

while True:
        X, Y = map(int, input().split())
        
        if X == Y == 0:
            break
            
        if Y % X == 0:
            print("factor")
        elif X % Y == 0:
            print("multiple")
        else:
            print("neither")
