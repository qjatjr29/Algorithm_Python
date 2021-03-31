import sys
from sys import stdin
sys.setrecursionlimit(1000001)

N=int(stdin.readline())

wine=[0,0,0]
dp=[0,0,0]
for i in range (0,N):
    number=int(stdin.readline())
    wine.append(number)

result=0

for i in range(3,N+3):
    curWine=max(dp[i-3]+wine[i-1]+wine[i],dp[i-2]+wine[i])
    maxWime=max(curWine,dp[i-1])
    dp.append(maxWime)
    result=max(result,maxWime)

print(result)



