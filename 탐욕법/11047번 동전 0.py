import sys
from sys import stdin

N,K=map(int,input().split())

coins=[]
for i in range(0,N):
    coin=int(stdin.readline())
    coins.append(coin)

result=0
index=N-1
while True:
    if K==0 :break
    if K-coins[index]>=0:
        result+= K//coins[index]
        K-=coins[index] * (K//coins[index])
    index-=1
        

print(result)
