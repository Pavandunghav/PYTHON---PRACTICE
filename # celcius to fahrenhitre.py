# celcius  to fahrenhitre 

def convert(c):
    
    
    f= (c * 9/5) + 32 
    
    print("temperature in fahrenite is :",f)
    
def main():
    c=int(input("enter celcius temperture :"))
    
    convert(c)
    
main()