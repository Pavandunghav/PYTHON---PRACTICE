l=[]
n=int(input("enter no. of students :"))

for i in range (n):
 a=int(input("enter your marks :"))
 l.append(a)
 print(l)

# average score of the class

avg=sum(l)/n

print("average marks of the class is :",avg)

# highest score and lowest score 

l.sort()


hs=l[-1]
ls=l[0]
print("the highest ecore of the class:",hs)
print("the lowest score of the class is :",ls)

#count of absent student 

ab=0
for i in range (n):
    if (l[i]==0) or (l[i]<0):
        ab=ab+1

print("no. of absent student is :",ab)

# display mark with highest count 
max=1

for i in range (0,n):
   
    freq=l.count(i)
    
    if (freq>max):
      max=freq
      re=i
    

print("highest count in the student list :",max)
print("element with highest count is :",re)

