n=int(input())

array=list(map(int,input().split()))

result=-1000
sumNumber=0

if max(array)>0 :
    for i in range(0,len(array)):
        sumNumber+=array[i]
        if (result<sumNumber):
            result=sumNumber
        # 배열의 최대값이 양수인데
        # 합이 음수가 되면 이건 최대값이 아니다.
        if sumNumber<0:
            sumNumber=0
        # result=max(result,sumNumber)
    print(result)

else: 
    result=max(array)
    print(result) 