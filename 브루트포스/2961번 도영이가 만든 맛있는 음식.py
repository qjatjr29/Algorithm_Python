Sour=[]
Bitter=[]
N=int(input())

_MAX=1000000000
count=0

for i in range(N):
    s,b=map(int,input().split())
    Sour.append(s)
    Bitter.append(b)

def food(count,SourTemp,BitterTemp):
    global _MAX
    if count==N:
        return
    
    s_temp=SourTemp * Sour[count]
    b_temp=BitterTemp + Bitter[count]
    gap=abs(s_temp-b_temp)
    if(_MAX>gap):
        _MAX=gap
    
    food(count+1,s_temp,b_temp)
    food(count+1,SourTemp,BitterTemp)

food(count,1,0)
print(_MAX)