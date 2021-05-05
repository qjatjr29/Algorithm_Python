import sys
from sys import stdin

N=int(stdin.readline())
result=[]
_map = [[0 for col in range(N)] for row in range(N)]
visited =[[False for col in range(N)] for row in range(N)]
for i in range(0,N):
    number=stdin.readline()
    for j in range(0,N):
        _map[i][j]=number[j]

count=0

def house(curX,curY):
    global _map
    global visited
    global result
    global count
    if curX<0 or curY<0 or curX>=N or curY>=N:
        return
    if visited[curX][curY]==True :
        return

    visited[curX][curY]=True
    if _map[curX][curY]=='1':
        count+=1
        house(curX-1,curY)
        house(curX+1,curY)
        house(curX,curY-1)
        house(curX,curY+1)
    else :
        return

for i in range(0,N):
    for j in range(0,N):
        if _map[i][j]=='1' and visited[i][j]==False:
            count=0
            house(i,j)
            result.append(count)

result.sort()
size=len(result)
print(size)
for i in range (0,size):
    print(result[i])


# print(map)