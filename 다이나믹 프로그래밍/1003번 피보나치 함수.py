import sys
from sys import stdin
sys.setrecursionlimit(1000001)
T=int(stdin.readline())

zeroCount=0
oneCount=0
d=[]

def fibo(n):
    global zeroCount
    global oneCount
    global d
    if(n<0):
        return 
    if(n==0):
        zeroCount+=1
        return
    elif(n==1):
        oneCount+=1
        return
    else:
        if d[n]>0:
            zeroCount+=1
            oneCount+=1
        d[n]=1
        fibo(n-1)
        fibo(n-2)

for i in range(0,T):
    N=int(stdin.readline())
    d=[0 for i in range(0,N+1)]
    zeroCount=0
    oneCount=0
    fibo(N)
    print(zeroCount,oneCount)
    