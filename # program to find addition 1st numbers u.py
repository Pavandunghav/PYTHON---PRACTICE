# program to find addition 1st numbers  using recursive functions 

def add_recursive(n):
    
    sum=(n*(n+1))/2
    
    return(sum)

def main():
     n=int(input("enter upto what you want addition :"))
     
     add_recursive(n)

     print(add_recursive(n))
main()