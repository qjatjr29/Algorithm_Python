import sys
from sys import stdin
sys.setrecursionlimit(1000001)
N=int(stdin.readline())

A = list(map(int,input().split()))

result=[ 1 for i in range (N)]

maxlength=1

for i in range(1,N):
    for j in range(0,i):
        if A[j]<A[i]:
            if result[j]+1>result[i]:
                result[i]=result[j]+1
    maxlength=max(maxlength,result[i])

print(maxlength)

