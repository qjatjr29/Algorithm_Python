import sys
N=  int(sys.stdin.readline())

# N=int(input())

# starMap=[[0 for col in range(N*2) ] for row in range(N)]
starMap=[" "*(N*2) for i in range(N)]


# 가운데에서 시작. N=24 ==> (x,y) --> (12,20)
form=["*","* *","*****"]

def printStar(N,x,y):
    global starMap
    if N==3:
        starMap[x]=starMap[x][:y]+form[0]+starMap[x][y+1:]
        starMap[x+1]=starMap[x+1][:y-1]+form[1]+starMap[x+1][y+2:]
        starMap[x+2]=starMap[x+2][:y-2]+form[2]+starMap[x+2][y+3:]
        return
    printStar(N//2,x,y)
    printStar(N//2,x+N//2,y-N//2)
    printStar(N//2,x+N//2,y+N//2)

startY = N-1
printStar(N,0,startY)


for _list in starMap:
    print(_list)