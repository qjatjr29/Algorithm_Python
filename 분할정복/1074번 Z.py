N,r,c=map(int,input().split())
r+=1
c+=1
result=0

def visited(row,col,N):
    global result
    add=pow(2,N-1)
    if(N==0):
        return

    # 아래 케이스에 있는 경우
    if row<r :
        result+=(add*add*2)
        # 오른쪽 아래 
        if col<c:
            result+=(add*add)
            visited(row+add//2,col+add//2,N-1)
        # 왼쪽 아래
        else:
            visited(row+add//2,col-add//2,N-1)
    
     # 위 케이스에 있는경우
    else:
        # 오른쪽 위
        if col<c:
            result+=(add*add)
            visited(row-add//2,col+add//2,N-1)
        # 왼쪽 위
        else:
            visited(row-add//2,col-add//2,N-1)


start=pow(2,N-1)

visited(start,start,N)
print(result)