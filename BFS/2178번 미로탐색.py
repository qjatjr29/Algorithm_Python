import sys
from sys import stdin

N,M = map(int,stdin.readline().split())
_map = [[0 for col in range(M)] for row in range(N)]
visited =[[False for col in range(M)] for row in range(N)]
for i in range(0,N):
    number=stdin.readline()
    for j in range(0,M):
        _map[i][j]=number[j]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
_count=1
check=False

def miro(curX,curY,count):
    global visited
    global _map
    global dx
    global dy
    global _count
    global check
    visited[curX][curY]=True
    _move=[]
    _move.append((count,(curX,curY)))
    while True:
        if len(_move)==0 :
            break
        mincount=_move[0][0]
        row=_move[0][1][0]
        col=_move[0][1][1]
        if row==N-1 and col==M-1:
            check=True
            _count=mincount
            break
        _move.pop(0)
        for i in range(0,4):
            _x=row+dx[i]
            _y=col+dy[i]
            if(_x<0 or _y<0 or _x>=N or _y>=M):
                continue

            if(_map[_x][_y]=='1' and visited[_x][_y]==False):
                visited[_x][_y]=True
                _move.append((mincount+1,(_x,_y)))
                

for i in range(0,N):
    if check==True:
        break
    for j in range(0,M):
        visited =[[False for col in range(M)] for row in range(N)]
        _count=1
        check=False
        if(_map[i][j]=='1'):
            miro(i,j,_count)
        if check==True:
            break

print(_count)


    