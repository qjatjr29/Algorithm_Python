import sys
from sys import stdin
sys.setrecursionlimit(1000001)
T=int(stdin.readline())

result="NO"

def move(x,y,N):
    global result
    global checkboard

    # 기저 사례
    # 범위를 넘어가서는 안된다.
    if x>=N or y>=N:
        return

    # 이미 도착한 경우가 생겼을 때
    if result=="YES":
        return 
    
     # 이미 왔던곳
    if checkboard[x][y]==True:
        return

    checkboard[x][y]=True
    # 아래 칸으로 이동했을 경우 x좌표 값
    move_X=Gameboard[x][y]+x
    # 오른쪽 칸으로 이동 했을 경우 y좌표값
    move_Y=Gameboard[x][y]+y

    # 도착한 경우 아래로 이동
    if move_X==N-1 and y==N-1 :
        result="YES"
        return
    # 도착한 경우 오른쪽으로 이동
    elif x==N-1 and move_Y==N-1:
        result="YES"
        return 
    else:
        move(move_X,y,N)
        move(x,move_Y,N)

# main 
for i in range(0,T):
    
    N=int(stdin.readline())
    # 매번 케이스 마다 초기화 
    # 전체 게임 판  좌표 : ( x : row ,y : col )
    Gameboard=[[0 for i in range(N)] for j in range (N)]
    #  왔던 땅인지 확인하는 배열
    checkboard=[[False for i in range(N)]for j in range(N)]
    for i in range(0,N):
        number=list(map(int,stdin.readline().split()))
        for j in range(0,N):
            Gameboard[i][j]=number[j]
    # 결과 초기화
    result="NO"
    move(0,0,N)

    print(result)

