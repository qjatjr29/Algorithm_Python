import sys
from sys import stdin

testCase=int(stdin.readline())

for i in range (0,testCase):
    N=int(stdin.readline())
    result=0
  
    russia=list(map(int,stdin.readline().split()))
    korea=list(map(int,stdin.readline().split()))
    
    russiaSort=sorted(russia)
    koreaSort=sorted(korea)

    # print(russiaSort)
    # print(koreaSort)

    # 러시아의 가장 작은 레이팅을 가진 선수보다
    # 우리팀이 그 선수 레이팅보다 높아진 경우를 구한다
    # 찾았으면 러시아 선수의 인덱스를 증가 시켜 준다.
    curindex=0
    russiaIndex=0
    for i in range(0,N):
       if(russiaSort[russiaIndex]<=koreaSort[i]):
           russiaIndex+=1
           result+=1
    
    print(result)
    



