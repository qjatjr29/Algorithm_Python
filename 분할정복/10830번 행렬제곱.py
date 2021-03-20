import sys
N,B= map(int,input().split())

matrix=[[0 for col in range(N) ] for row in range(N)]
tempMatrix=[[0 for col in range(N) ] for row in range(N)]

for i in range(0,N):
    temp=[]
    temp=list(map(int,input().split()))
    for j in range(0,N):
        if temp[j]==1000:
            temp[j]=0
        matrix[i][j]=temp[j]
        tempMatrix[i][j]=temp[j]


def PowMatrix():
    global matrix
    __Matrix=[[0 for col in range(N) ] for row in range(N)]
    for i in range(0,N):
        for j in range(0,N):
            number=0
            for z in range(0,N):
                number+=matrix[i][z]*matrix[z][j] % 1000
            number=number%1000
            if number==1000:
                number=0
            __Matrix[i][j]=number
    matrix=__Matrix

def MultiplyMatrix():
    global matrix
    __Matrix=[[0 for col in range(N) ] for row in range(N)]
    for i in range(0,N):
        for j in range(0,N):
            number=0
            for z in range(0,N):
                number+=matrix[i][z]*tempMatrix[z][j] % 1000
            number=number%1000
            if number==1000:
                number=0
            __Matrix[i][j]=number
    matrix=__Matrix

def solve(B):
    global matrix
    if B==1:
        return
    # n 홀수
    if B%2==1:
        B-=1
        solve(B//2)
        PowMatrix()
        MultiplyMatrix()
    else:
        solve(B//2)
        PowMatrix()
    return

solve(B)

for i in range(0,N):
    for j in range(0,N):
        print(matrix[i][j],end=" ")
    print("")
