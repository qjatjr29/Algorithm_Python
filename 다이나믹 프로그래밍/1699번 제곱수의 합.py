import sys
from sys import stdin
sys.setrecursionlimit(1000001)
N=int(stdin.readline())

dp = [i for i in range(N+1)]

for i in range(1,N+1):
    curIndex=1
    while True:
        if curIndex*curIndex>i:
            break
        if dp[i]>dp[i-curIndex*curIndex] +1 :
            dp[i]=dp[i-curIndex*curIndex]+1
        
        curIndex+=1

print(dp[N])


    