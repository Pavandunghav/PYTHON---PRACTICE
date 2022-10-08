# create a blank list and take input from user for elements and find the average of the all elements 

a=int(input("enter no. of elements you want to add"))

b=[]

for i in range(0,a):

    c=int(input("enter a element"))
    b.append(c)
    i=i+1

print(b)

#sum =0
'''for j in range(0,a):
    
     sum=b[j]

     j=j+1
print(sum)

avg=sum/a
print(avg)'''

'''x=sum(b)
print(x)
avg=x/a'''

avg2=sum(b)/a
print(avg2)