import sys
from sys import stdin

N=int(stdin.readline())

T=[1,3]

for i in range(2,N):
    number=((T[i-2]*2)%10007+T[i-1]%10007) % 10007
    T.append(number)

print(T[N-1])
