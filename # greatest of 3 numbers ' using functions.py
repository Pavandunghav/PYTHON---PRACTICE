# greatest of 3 numbers '

def great():
    
    if (n1>n2) and (n1>n3):
        print("greatest number is :",n1)
    
    elif (n2>n1)  and (n2>n3):
          print("greatest number is :",n2)
          
    else:
        print( print("greatest number is :",n3))
        
        
def main():
    
    global n1,n2,n3
    n1=int(input("enter a first number :"))
    n2=int(input("enter a second  number :"))
    n3=int(input("enter a third  number :")) 
         
    great()
    
main()