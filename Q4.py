mylist=[]
#Taking input untill user enters -1
while(1):
    elem=input('Enter Element')
    if(elem=='exit'):
        break
    else:
        mylist.append(elem)

#mylist items
print(mylist)
print(type(mylist[0]))

for i in mylist:
    if (isinstance(i,int)):
        print('int')
    else:
        print('str')    