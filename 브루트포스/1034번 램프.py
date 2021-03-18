N,M =map(int,input().split())

map=[]

for i in range(N):
    rowInput=input()
    map.append(rowInput) 
    # 0101 이런식으로 string 형식으로 들어오겠찌..?

# 행렬의 각각 행 을 다 비교 해봐야 할듯.
# 행렬중에 같은 모양의 행이 있으면 한번에 많이 올릴 수 있다.
# 만약 한 행에 안켜진게 3개인데 K가 4 이면 그 행은 어떻게 해도 못킴
# K가 짝수면 행에 안켜진 곳도 짝수여야 그 쪽 킬 수 있다.
# K가 2의 배수인 경우 일때 아닐때 나눠서 풀자.
K=int(input())
maxLamp=0


for y in range(0,N):
    # 각 행의 안켜진것 개수 check
    count=0
    # 킬 수 있는 램프의 수
    # 현재 행 
    lamp_count=1
    x=y

    for Z in range(0,M):
        if(map[y][Z]=='0'):
            count+=1

    if(count>K):
        continue
    if(count%2 == K%2):
        for j in range(x+1,N):
            if(map[y]==map[j]):
                lamp_count+=1

        if lamp_count>maxLamp:
            maxLamp=lamp_count

print(maxLamp)
    
       
