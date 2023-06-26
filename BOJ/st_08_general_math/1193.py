a,b,c=1,1,1		#c는 불필요한 반복을 제거하기 위해 사용
d=1			#방향
e=int(input())
while(e>0):
    e-=c		
    c+=1		#입력된 수에 c를 빼고, c에 1을 더한다.
    d=-d		#방향 전환
c-=1			
e+=c			#마지막에 저장된 c와 e에서 한 단계 물러준다.
if d==1:
    b=c
    for i in range(e-1):
        b-=1
        a+=1
else:
    a=c
    for i in range(e-1):
        b+=1
        a-=1
print(a,"/",b,sep="")
