import random
com=["rock","paper","scissor"]
point1=0
point2=0
inp="yes"
while(inp=="yes"):
    print("                   **********Rock - Paper - Scissor - Game*********")
    cominput=random.choice(com)
    print("1.Rock\n2.Paper\n3.Scissor")
    print("Enter your choice :",end="")
    uinput=input().lower()
    print("Computer's choice is :",cominput)
    if(uinput=="rock"):
        if(cominput=="paper"):
            print("\nYou Lose...!\n")
            point2+=1
        elif(cominput=="scissor"):
            print("\nYou Won...!\n")
            point1+=1
        else:
            print("\nIts a Tie...!\nTry again\n")
    elif(uinput=="paper"):
        if(cominput=="scissor"):
            print("\nYou Lose...!\n")
            point2+=1
        elif(cominput=="rock"):
            print("\nYou Won...!\n")
            point1+=1
        else:
            print("\nIts a Tie...!\nTry again....\n")
    elif(uinput=="scissor"):
        if(cominput=="rock"):
            print("\nYou Lose...!\n")
            point2+=1
        elif(cominput=="paper"):
            print("\nYou Won...!\n")
            point1+=1
        else:
            print("\nIts a Tie...!\nTry again...\n")
    else:
        print("select one among the above three\n")
    print("<---------Score--------->")
    print("Your Score is :",point1)
    print("Your opponent score is :",point2)
    print("\nDo you want to try again")
    print("Yes/No\n")
    inp=input().lower()
    if(inp=="no"):
        break
    elif(inp=="yes"):
        continue
    else:
        print("Enter a valid choice")
        continue
        
print("\n                 <------------------------Your game has been completed----------------------->\n")
if(point1>point2):
    print("\n                                        *****You Won in the Match*****\n")
elif(point1<point2):
    print("\n                                        *****You Lost the Match*****\n")
else:
    print("\n                                        *****The Match is Tie*****\n")
print("\n                 <----------------------------------Score------------------------------------->")     
print("                                             Your Score :",point1)
print("                                             opponent Score :",point2)
        

