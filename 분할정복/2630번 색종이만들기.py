N=int(input())


ColorPaper=[[0 for col in range(N) ] for row in range(N)]
for paperX in range(0,N):
    papers= list(map(int,input().split()))
    for paperY in range(0,N):

        ColorPaper[paperX][paperY]=papers[paperY]

WhiteColor=0
BlueColor=0

def FindPaper(N,x,y):
    global WhiteColor
    global BlueColor
    color=ColorPaper[x][y]
    
    if N==1:
        if color==1:
            BlueColor+=1
        else :
            WhiteColor+=1
        return
    
    check =True

    for i in range(0,N):
        if check==False:
            break
        for j in range(0,N):
            if(color!=ColorPaper[x+i][y+j]):
                check=False
                break
    
    if check:
        if color==1:
            BlueColor+=1
        else :
            WhiteColor+=1
        return
    
    FindPaper(N//2,x,y)
    FindPaper(N//2,x+N//2,y)
    FindPaper(N//2,x,y+N//2)
    FindPaper(N//2,x+N//2,y+N//2)

FindPaper(N,0,0)
print(WhiteColor)
print(BlueColor)