N = int(input())

starMap=[[0 for col in range(N) ] for row in range(N)]
for starx in range(0,N):
    for stary in range(0,N):
        starMap[starx][stary]=" "




def Divide(N,x,y):
    global starMap
    # 3 X 3 행렬 이 되었을 때 기저 사례 !
    if N==3:
        for i in range(0,3):
            for j in range(0,3):
                if(i==1 and j==1): 
                    continue
                starMap[i+x][j+y]="*"
        return
    

    #  9 개 구역으로 나눈다.  ==> 8개 구역 들어감.
    
    # 왼쪽  위
    Divide(N//3, x,y)
    # 왼쪽 위
    Divide(N//3,x+N//3,y)
    # 오른쪽 위
    Divide(N//3,x+(N//3*2),y)
    #왼쪽  중간
    Divide(N//3,x,y+N//3)
    # 가운데--> X안들어감
    #오른쪽 중간
    Divide(N//3,x+(N//3*2),y+N//3)
    #왼쪽 아래
    Divide(N//3,x,y+(N//3*2))
    # 아래
    Divide(N//3,x+N//3,y+(N//3*2))
    # 오른쪽 아래
    Divide(N//3,x+(N//3*2),y+(N//3*2))

Divide(N,0,0)

for i in range(0,N):
    for j in range(0,N):
        print(starMap[i][j],end="")
    print("")