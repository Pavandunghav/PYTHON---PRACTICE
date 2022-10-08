# write a python  program to show eligibility to work 
# given condition : only girls with age greater than 20 allowed to work 

a=int(input(" enter your age "))
b=chr(input(" enter you gender as G for girls and B for boys "))

if(a>20) and (b=="G"):
    print(" you are eligible to work ")

else :
    print (" you are not eligible ")