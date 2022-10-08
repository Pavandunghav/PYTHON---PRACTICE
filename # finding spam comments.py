# finding spam comments   word in the comments 
# given : money , buy , subscribe , click 


l1=[]

n=int(input("enter a no. of words or elements to be in spam comment:"))

for i in range (0,n):
    a=str(input(" enter a any elements to be in spam comment :"))

    l1.append(a)

print(l1)

comments=str(input(" enter a comment: "))

for i in range(0,n):
    
 if  ((l1[i]) in (comments)) :

    print("your comment is spam.please enter valid comment  ")

 else:
    print(" thank you so much for comment ")

    i=i+1
    

