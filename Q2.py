outer=[]#inititalize empty list  for outer
#taking input for no of elements
row=int(input("Enter rows"))
for i in range(row):
    inner=[] #empt list for nested element
    while(True):
        num=int(input("Enter number"))
        if(num<=0):
            break
        else:
            inner.append(num)
    outer.append(inner) #merging inner and outer list 

print(outer)
#find the length and append it to new list called lenlist
lenList=[]
for i in outer:
   lenList.append(len(i)) 
print(lenList)   