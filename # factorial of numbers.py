# factorial of number 

n=int(input(" enter a number to get its factorial:"))
fact=1
for i in range(1,n):
    fact=fact*i
    i=i+1

print( fact)