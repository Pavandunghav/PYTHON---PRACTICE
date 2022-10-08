# take marks  for 4 subjects and total marks from user 
# write a program to find out whether student is pass or fail
#given condition : it requires total 40% and atleast 33% in each subject to pass.

m=int(input(" enter your marks in maths "))
p=int(input(" enter your marks in physics "))
b=int(input(" enter your marks in biology "))
c=int(input(" enter your marks in chemistry "))
t=int(input(" enter your marks in total "))

if(m>33)and(p>33)and(b>33)and(c>33)and(t>40):
    print(" congrats bro , you are pass")

else:
    print(" ohhh sorry , you are fails , keep trying , all the best ")


