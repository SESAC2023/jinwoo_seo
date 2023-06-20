# find 함수는 찾는 문자가 문자열 안에서 있다면 첫 번째에 위치한 순서를 숫자로 출력
# 찾는 문자가 문자열 안에 없으면 -1 출력 

s = str(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet: 
    print(s.find(i), end = " ")
