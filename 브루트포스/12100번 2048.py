# 움직이는 방향쪽에 가기전에 블록이 앞에 있는지 확인
# 블록이 있다면 그 블록이 나랑 같은 값인지 확인
# 같은 값이면 가려는 쪽으로 숫자 2배 되면서 합쳐짐
# 블록이 없다면 한칸 움직이고 다시 반복.

#  가려는 방향의 맨 끝점 (도착점)에서 멀어지는 순으로 시작할것.
# 그니깐... 위로 가는 방향이면 0번째 행부터 확인 하면서 가기... 이게 마지막 조건
# 이미 합쳐진거면 다시 못합친다.. (한번 움직일때)

N =int(input())

gameboard=[]
MaxBlock=0
for i in range(0,N):
    inputNum= list(map(int,input().split()))
    temp_map=[]
    for j in range(0,N):
        temp_map.append(inputNum[j])
    gameboard.append(temp_map)

def move_right():
    queue = []
    global gameboard
    # 큐 에 값 다 저장 해놓고
    # 첫행 오른쪽 부터 <-- 순으로 저장.
    for i in range(0,N):
        for j in range(N-1,-1,-1):
            if gameboard[i][j] :
                queue.append(gameboard[i][j])
            gameboard[i][j]=0
        curindex=N-1
        while(1):
            if len(queue)==0: break

            block=queue[0]
            del queue[0]

            if gameboard[i][curindex]==0:
                gameboard[i][curindex]=block
            elif gameboard[i][curindex]==block:
                gameboard[i][curindex]*=2
                curindex-=1
            else:
                curindex-=1
                gameboard[i][curindex]=block
                
        
def move_up():
    queue = []
    global gameboard
    # 큐 에 값 다 저장 해놓고
    # 첫행부터 <-- 순으로 저장.
    for i in range(0,N):
        for j in range(0,N):
            if gameboard[j][i]:
                queue.append(gameboard[j][i])
            gameboard[j][i]=0
        curindex=0
        while(1):
            if len(queue)==0: break

            block=queue[0]
            del queue[0]

            if gameboard[curindex][i]==0:
                gameboard[curindex][i]=block
            elif gameboard[curindex][i]==block:
                gameboard[curindex][i]*=2
                curindex+=1
            else:
                curindex+=1
                gameboard[curindex][i]=block
                
    
        
def move_left():
    queue = []
    global gameboard
    # 큐 에 값 다 저장 해놓고
    # 첫행부터 <-- 순으로 저장.
    for i in range(0,N):
        for j in range(0,N):
            if gameboard[i][j]:
                queue.append(gameboard[i][j])
            gameboard[i][j]=0
        curindex=0
        while(1):
            if len(queue)==0: break

            block=queue[0]
            del queue[0]

            if gameboard[i][curindex]==0:
                gameboard[i][curindex]=block
            elif gameboard[i][curindex]==block:
                gameboard[i][curindex]*=2
                curindex+=1
            else:
                curindex+=1
                gameboard[i][curindex]=block
                

def move_down():
    queue = []
    global gameboard
    # 큐 에 값 다 저장 해놓고
    # 
    for i in range(0,N):
        for j in range(N-1,-1,-1):
            if gameboard[j][i]:
                queue.append(gameboard[j][i])
            gameboard[j][i]=0
        curindex=N-1
        while(1):
            if len(queue)==0: break

            block=queue[0]
            del queue[0]

            if gameboard[curindex][i]==0:
                gameboard[curindex][i]=block
            elif gameboard[curindex][i]==block:
                gameboard[curindex][i]*=2
                curindex-=1
            else:
                curindex-=1
                gameboard[curindex][i]=block
                

def move(dir):
    if dir==0:
        move_right()
    elif dir==1:
        move_up()
    elif dir==2:
        move_left()
    else:
        move_down()


def DFS(moveCount):
    global MaxBlock
    global gameboard
    if moveCount==5:
        for i in range(0,N):
            for j in range(0,N):
                MaxBlock=max(MaxBlock,gameboard[i][j])
        return

    curGameBoard=[]
    for i in range(0,N):
            temp_board=[]
            for j in range(0,N):
                temp_board.append(gameboard[i][j])
            curGameBoard.append(temp_board)
    
    for i in range(0,4):
        move(i)
        DFS(moveCount+1)
        
        gameboard=[]
        for j in range(0,N):
            temp__board=[]
            for z in range(0,N):
                temp__board.append(curGameBoard[j][z])
            gameboard.append(temp__board)

DFS(0)
print(MaxBlock)
