number=list(map(int,input().split()))
N=number[0]
jimin=number[1]
hansoo=number[2]

result=0
count=0

if N%2 !=0:
    count+=1

while True:
    if N==1:
        break
    N = N//2
    count+=1

for i in range(count+1):
    if(abs(jimin-hansoo) ==1 ) and (jimin//2 != hansoo//2 ):
        result+=1
        break
    else:
        jimin=(jimin+1)//2
        hansoo=(hansoo+1)//2
        result+=1

print(result)


'''
check=False
result=0
_list=[]
# 처음 리스트에 값 넣어주기.
for i in range(0,N):
    _list.append(i)

jimin-=1
hansoo-=1
'''
'''
def move(person):
    if person&2==0:
        return person//2
    else:
        return person//2+1

# 지민이랑 한수는 속 움직일때마다 번호가 바뀐다

while True:
    if(abs(jimin-hansoo)==1 and jimin//2 != hansoo//2 ):
        break

    else:
        a=move(a)
        b=move(b)
        result+=1

print(result)
'''


'''
while(True):
    _size=len(_list)
    if check:
        break
    if _size<2:
        break

    # 짝수명일때.
    if _size%2==0:    
        for i in range(0,_size//2):
            a=_list[0]
            b=_list[1]
            if ((a==jimin and b==hansoo) or (a==hansoo and b==jimin)):
                check=True
                break

            if((a==jimin) or (b==jimin)):
                _list.append(jimin)
                _list.remove(a)
                _list.remove(b)
            elif((a==hansoo)or(b==hansoo)):
                _list.append(hansoo) 
                _list.remove(a)
                _list.remove(b)   
            else:
                _list.remove(a)
                _list.remove(b)
                _list.append(a)
            

    # 홀수명일때
    else:
        temp = _list[_size-1]
        for i in range(0,_size//2):
            a=_list[0]
            b=_list[1]
            if ((a==jimin and b==hansoo) or (a==hansoo and b==jimin)):
                check=True
                break

            if(a==jimin or b==jimin):
                _list.append(jimin)
                _list.remove(a)
                _list.remove(b)
            elif(a==hansoo or b==hansoo):
                _list.append(hansoo) 
                _list.remove(a)
                _list.remove(b)   
            else:
                _list.remove(a)
                _list.remove(b)
                _list.append(a)

        _list.append(temp)
    
    result+=1

if check : 
    print(result)
else:
    print(-1)
'''