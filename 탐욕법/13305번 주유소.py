import sys
from sys import stdin

N=int(stdin.readline())

distance=[]
Cost=[]
dist=list(map(int,input().split()))
co=list(map(int,input().split()))

for i in range(0,N-1):
    distance.append(dist[i])

for i in range(0,N):
    Cost.append(co[i])

CurrentIndex=0
count=1
result=0
while True :
    if count==N:
        break
    result+=Cost[CurrentIndex]*distance[count-1]
    if Cost[CurrentIndex]>Cost[count]:
        CurrentIndex=count
    
    count+=1


print(result)
