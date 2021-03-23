import sys
from sys import stdin
sys.setrecursionlimit(1000001)
T = int(stdin.readline())
MAXNUM=1000000009

dp=[0 for i in range(1000001)]
dp[0]=1
dp[1]=1
dp[2]=2
for i in range(3,1000001):
    dp[i]=int((dp[i-1]%MAXNUM+dp[i-2]%MAXNUM+dp[i-3]%MAXNUM)%MAXNUM)


for i in range(0,T):
    n=int(stdin.readline())
    print(dp[n])







