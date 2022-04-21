#Q.1. Write a Python program to create a list of numbers by taking input from the user and then remove  the duplicates from the list.
# You can take input of non-zero numbers, with an appropriate  prompt, from the user until the user enters a zero to create the 
 #list assuming that the numbers  are non-zero.
  #  Sample Input: [10, 34, 18, 10, 12, 34, 18, 20, 25, 20]  
   # Output: [10, 34, 18, 12, 20, 25]  

num_list=[]
while(True):
    num=int(input("Enter a number greater than zero"))
    if(num==0 or num<0):
        break
    else:
        num_list.append(num)
print("Elements are:-")
print(num_list)
repeat=[]
for i in num_list:
    if i not in repeat:
        repeat.append(i)

print("After Removing Duplicate Elements:-")
print(repeat)






