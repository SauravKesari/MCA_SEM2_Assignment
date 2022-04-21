#list declaration
num_list=[]
#temporary list for converting element into tuples type
newlist1=[] #used for even element
newlist2=[] #used for odd element
#tuples declaration
odd=()
even=()
#Taking user input until he/she enteres zero or less than zero value
while(True):
    num=int(input("Enter Elememts"))
    if num<=0:
        break
    else:
        num_list.append(num)
print(num_list)
#spliting the list into even odd part
for i in num_list:
    if(i%2==0):
        newlist1.append(i)
        even=tuple(newlist1)
    else:
        newlist2.append(i)
        odd=tuple(newlist2)    

#Displaying result to user
print("Even Elements:- ",even)
print("Odd Elements:- ",odd)        
        
