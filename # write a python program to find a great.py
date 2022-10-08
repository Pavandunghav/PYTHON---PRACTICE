# write a python  program to find a greatest of four no. entered by the user 

a=int(input(" enter your first number: "))
b=int(input(" enter your second number :"))
c=int(input(" enter your three number :"))
d=int(input(" enter your fourth number: "))

if(a>b) and (a>c)and(a>d):
    print(a)
    print(" is a gretest number ")

if(b>a) and (b>c)and(b>d):
    print(b)
    print(" is a gretest number ")

if(c>b) and (c>a)and(c>d):
    print(c)
    print(" is a gretest number ")

else:
    print(d)
    print(" is greatest number")