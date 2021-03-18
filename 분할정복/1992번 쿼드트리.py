N = int(input())
result=""

TreeMap=[]


# 원래 트리 배열 값 저장.
for i in range(0,N):
    inputNum= list(map(int,input()))
    temp_map=[]
    for j in range(0,N):
        temp_map.append(inputNum[j])
    TreeMap.append(temp_map)

# 트리는  (좌표 : (y,x)) y가 열 x 가 행

def divideConquer(size,x_index,y_index):
    global result
    # 기저 사례
    if size==1:
        return TreeMap[x_index][y_index]
    
    # size만큼 반복문 돌아서 다 같은 값인지 확인 하기 위한 변수
    check_one=True
    check_zero=True

    for i in range(x_index,x_index+size):
        for j in range(y_index,y_index+size):
            if TreeMap[i][j]==1:
                check_one=False
            else:
                check_zero=False
    
    # check_one 이 true 면 1이 있었다
    # check_zero 가 true 면 0이 있었다.
    # 따라서 둘다 true인 경우면 1/4으로 분할해야 한다.
    
    # 만약 check_one 이 false , check_zero 가 true 인 경우
    # 이 구간에는 다 1 값만 가지는 것이니 result += 1해준다.
    # 물론 더 들어갈 필요도 없다. 따라서  재귀함수 나가야함 --> return
    # 반대의 경우는 result += 1 

    #이 과정 반복


    if(check_one):
        return 0
    
    if(check_zero):
        return 1

    # 1/4으로 나누는 과정
    temp=""
    # 왼쪽 위
    LUtemp=divideConquer(size//2,x_index,y_index)
    # 오른쪽 위
    RUtemp=divideConquer(size//2,x_index,y_index+size//2)
    # 왼쪽 아래
    LDtemp=divideConquer(size//2,x_index+size//2,y_index)
    # 오른쪽 아래
    RDtemp=divideConquer(size//2,x_index+size//2,y_index+size//2)
    temp+="("+f"{LUtemp}"+f"{RUtemp}"+f"{LDtemp}"+f"{RDtemp}"+")"
   
    return temp


result=divideConquer(N,0,0)

print(result)