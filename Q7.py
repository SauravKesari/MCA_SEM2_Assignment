stringList=[]
while(1):
    words=input("Enter the words")
    if(words=='exit'):
        break
    else:
        stringList.append(words)
print(stringList)   



def frequency(wordList):
    mydic={}
    for i in wordList:
        if(i in mydic):
            mydic[i]+=1
        else:
            mydic[i]=1
    print(50*'=')
    print("----------------Dictionary is:---------------")        
    print(mydic)
    print(50*'=')
    for i in wordList:
        if(mydic[i]!=0):
            print("words are {} comes {} times".format(i,mydic[i]))
            mydic[i]=0


frequency(stringList)
        
