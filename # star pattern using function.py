# star pattern using function 

def directstar(n):
    pa="*"
    for i in range (1,n+1,1):
        
     pa=("*"*i)
     print(pa)
    
def reversestar(n):
    
   
    
    for i in range (n,0,-1):
        
        pa="*"*i
        print(pa)
    
    
def main():
   
   
    
    flag="yes"
    
    while(flag=="yes"):
      n=int(input("enter a number of lines:"))
      ch=int(input("enter a choice (1] straight pattern  2] reverese pattern "))
        
      if (ch==1):
        directstar(n)
      elif(ch==2):
        reversestar(n)
      else:
        print("enter valid choice :")
        
      flag=str(input("do you want to continue (yes/no)? :"))

main()