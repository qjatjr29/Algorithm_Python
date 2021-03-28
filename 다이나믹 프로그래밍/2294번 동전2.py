import sys
from sys import stdin
n=int(stdin.readline())


count=0



while True:
    if n<0:
        break
    if n%5==0:
        count+=n//5
        print(count)
        break
    if n>=2:
        count+=1
        n-=2
    else:
        print(-1)
        break

   
    