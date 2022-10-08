l=[]
n=int(input("enter how many persons you want to add in the list: "))

for i in range(0,n):
    p=str(input("enter a name of person:"))
    l.append(p)
    print(l)

for j in l:

   if j.startswith("s"):
        print(j," hello , you are welcome")



'''  if ("l" in l[j]):
        print(l[j]," hello,you are  welcome in the party:")

    else:
        print("are not welcome")'''