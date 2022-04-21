student={}
while(1):
    roll=int(input("Enter roll number"))
    if(roll<1):
        break
    else:
        marks=[]
        for i in range(3):
                mark=int(input("Enter marks"))
                if(mark>=0 and mark<=100):
                    marks.append(mark)
                else:   
                    print("Not valid Number")
                       
        student[roll]=marks
print(student)        
line=50*'='
print(line)
print("\nRollNo\t Mark1\t Mark2\t Mark3\t Total")
tot = 0

for r in student:
    print(r,"\t",end=" ")
    for m in student[r]:
        tot = tot + m
        print(m,"\t",end=" ")
    print(tot)
    tot = 0

