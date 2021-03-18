stringList=input().split()
X=stringList[0]
Y=stringList[1]

gap = len(Y)-len(X)
min_alpha =51
#position=0

for i in range (gap+1):
    min_temp=0
    for j in range (len(X)): 
        if(X[j] != Y[i+j]):
            min_temp+=1
    if(min_alpha>min_temp):
        min_alpha=min_temp
        #position=i   
#loopcount=0

print(min_alpha)

'''
 while(1):
     if loopcount==gap:
         break
     pre_count=0
     post_count=0
     if(position-1<0 and position+1>=len(Y)):
         temp_x=Y[position-1]+X
         temp__x=X+Y[position+1]
         for i range(len(temp_x)):
'''       
