
s=str(input("enter a string:"))
# to display word with longest length
l=s.split()
def longestword():
    

    longest=0

    for i in (l):

        if(longest<len(i)):

            longest=len(i)
            lg=i
        else:
            continue
          
    print("length of longest word in string is ",longest)
    print(" longest word in string is ",lg)
longestword()
    
# frequency of particular character 

def fch():
    b=str(input(" enter a character to find in string :"))
    f=0
    for j in l:

        if (j==b):
            f=f+1
        
    print(" frequency of character is :",f)

fch()

# palindrome or not 

def palindrome ():

 for k in range (0,len(s)):

    for d in range (len(s),0,(-1)):


        if (k==d):
            
            v="string is palindrome"
            continue
        else:
            v="string is not palindrome "

 print(v)

palindrome()

# finding occurence of particular word 
def fw():
    b=str(input(" enter a character to find in string :"))
    f=0
    for j in l:

        if (j==b):
            f=f+1
        
    print(" frequency of character is :",f)

fw()


    

