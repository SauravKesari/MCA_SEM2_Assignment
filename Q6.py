

def frequencyEachchar(s):
    mydic={}
    #if item is  present in dictionary then add frequency
    for i in s:
        if i in mydic:
            mydic[i]+=1
        else:
            mydic[i]=1
    #Print in the same order in which they are entered
    print(mydic)
    for i in s:
        #Print only if characteres are not printed before
        if(mydic[i]!=0):
            print("{} is {} times".format(i,mydic[i]))
            #After printing all elements frequency sets to Zero
            mydic[i]=0


#Taking Input from user
str1=input("Enter string")
frequencyEachchar(str1)   
# d = Counter(str1)
# print(type(d)) 
#     # Print characters and their frequencies in
#     # sam order of their appearance
# for  i in d:
#     print(i+str(d[i]), end=" ")

