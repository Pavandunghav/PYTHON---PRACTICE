def fact(n):
    
    fact=1
    for i in range (1,n+1,1):
        fact=fact*(i)
        
    print(fact)
    
def main():
    
    n=int(input("enter a number :"))
    
    fact(n)
    
main()   