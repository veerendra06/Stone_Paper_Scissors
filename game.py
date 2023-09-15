 ### Game stone Paper scissors ###
 
import random

L = ("Rock","paper","scissor")

while True:
     ccount=0
     ucount=0
     uc = int(input('''
                    Game start
                   1. YES
                   2. NO
                
            
                    '''))
     if uc ==1:
         for a in range(1,4):
             user_input = int(input('''
     1 Rock
     2 Paper
     3 Scissor
                                   
                         '''))
             if user_input==1:
                 uchoice = "Rock"
             elif user_input==2:
                 uchoice = "paper"
             elif user_input==3:
                 uchoice = "scissor"
                
             Cchoice =random.choice(L)
            
             if Cchoice == uchoice:
                 print("Computer Score :" ,Cchoice)
                 print("Your score :",uchoice)
                 print("GAME OVER")
                
                 ucount=ucount+1
                 ccount=ccount+1
             elif (uchoice=="Rock" and Cchoice=="scissor" ) or(uchoice == "paper" and Cchoice =="Rock") or (uchoice=="scissor" and Cchoice =="paper"):
                
                 print("Computer Score :",Cchoice)
                 print("user value",uchoice)
                 print("You are a Winner") 
                 ucount=ucount+1
            
             else:
                 print("Computer Score :" ,Cchoice)
                 print("user_input",uchoice)
                 print("Computer Win")
                 ccount = ccount+1
                
         if ucount == ccount:
                  print("Computer Score :" ,ccount)
                  print("your score :",ucount)
                  print("Final draw")
                
         elif  ucount > ccount:
                  print("Computer  Score :" ,ccount)
                  print("Your Score :",ucount)
                  print("Final You are a winner....!!!") 
         else: 
                  print("computer Score :" ,ccount)
                  print("your Score :",ucount)
                  print("Final computer Win") 
                
                
                
     else:
         break
                
                  