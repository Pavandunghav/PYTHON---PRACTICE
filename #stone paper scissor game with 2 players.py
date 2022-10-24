# stone paper scissor with 1 player  and computer 

def game(player1,playerc):
    
     if(player1=="s" and playerc==1):
       result="tie"
       flag="yes"
       
     if(player1=="s" and playerc==2):
        result="playerc"
     if(player1=="s" and playerc==3):
         result="player1"
     
     
     
     
     if(player1=="p" and playerc==1):
         result="player1"
     
     if(player1=="p" and playerc==2):
        result="tie"
     if(player1=="p" and playerc==3):
         result="playerC"
     
     
     
     if(player1=="sc" and playerc==1):
         result="playerc"
     
     if(player1=="sc" and playerc==2):
        result="player1"
     if(player1=="sc" and playerc==3):
         result="tie"
         flag="yes"
      
     return(result)
     
     
     
     
     
def main():
    import random
    flag="yes"
    
    while(flag=="yes"):
      player1=str(input("1]stone(s)  2]paper(p)  3]scissor(sc): "))
      playerc=random.randint(1,3)
      print("computers choice is :",playerc)
      a=game(player1,playerc)
        
      print("the winner is :",a)
    
      flag=str(input("do you want to continue (yes/no)?"))
    
main()