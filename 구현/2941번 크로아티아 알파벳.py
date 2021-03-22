word =input()

check=0
result =0

while (1):
    if check>=len(word):
        break

    if check==len(word)-1:
        result+=1
        break

    if check<len(word)-2:
        if word[check]=='d'and word[check+1]=='z'and word[check+2]=='=':
            result+=1
            check+=3
            continue
            


    if check<len(word)-1:
        if word[check]=='c':
            if word[check+1]=='=':
                check+=1
            elif word[check+1]=='-':
                check+=1
        elif word[check]=='d':
            if word[check+1]=='-':
                check+=1
        
        elif word[check]=='l' and word[check+1]=='j':
            check+=1
        
        elif word[check]=='n'and word[check+1]=='j':
            check+=1
        elif word[check]=='s'and word[check+1]=='=':
            check +=1
        elif word[check]=='z'and word[check+1]=='=':
            check+=1
        check+=1
        result+=1
   

print(result)
