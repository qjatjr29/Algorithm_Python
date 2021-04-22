import sys
from sys import stdin
N,M=map(int,input().split())

mapList = [[0 for col in range(N+1)] for row in range(N+1)]
number= [0]*(N+1)
for i in range(1,N+1):
    number[i] =[0]+list(map(int, stdin.readline().split()))
for i in range(1,N+1):
    for j in range(1,N+1):
        mapList[i][j]=(number[i][j]+mapList[i-1][j]+mapList[i][j-1]-mapList[i-1][j-1])


for i in range(0,M):
    x1,y1,x2,y2=map(int, stdin.readline().split())
    print(mapList[x2][y2]-mapList[x2][y1-1]-mapList[x1-1][y2]+mapList[x1-1][y1-1])
   