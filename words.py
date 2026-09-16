sentence="i am shreya"
count=0
inword=False
for i in sentence:
    if(i!=" "and not inword ):
        inword=True
        count+=1
    elif(i==" " ):
        
        inword=False
print("number of words are",count)
