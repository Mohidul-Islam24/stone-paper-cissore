import random
def print_choice():
    print("choisee 1 for stone: ")
    print("choisee 2 for scissor: ")
    print("choisee 3 for paper: ")

def score_user():
    us_score=+1
    print("your score is: ",us_score)
    print("system score is: ",sy_score)

def score_sys():
    sy_score=+1
    print("system score is:",sy_score)
    print("user score is:",us_score)

print("Welcome to Stone,Paper,Scissor game")
option = True
us_score=0
sy_score=0

while(option):
    print_choice()
    us_ch = int(input("enter your choice: "))
    if us_ch==1:
        print("you have choice stone")

    elif us_ch==2:
        print("you have choice scissor")

    elif us_ch==3:
        print("you have choice paper")

    else:
        print("invilade choice")
        continue

    print("Now it's time for the system to chosee it's option")
    sy_ch=random.randint(1,3)
    if sy_ch==1:
        print("System have choice stone")

    elif sy_ch==2:
        print("System have choice scissor")

    elif sy_ch==3:
        print("System have choice paper")

    else:
        print("invilade choice")
        continue

    if us_ch==sy_ch:
        print("Drow this round")

    elif us_ch==1 and sy_ch==2:
        print("user win this round")
        score_user()
    elif us_ch==2 and sy_ch==3:
        print("user win this round")
        score_user()
    elif us_ch==3 and sy_ch==1:
        print("user win this round")
        score_user()
    else:
        print("system win this round")
        score_sys()

    if us_score<5 and sy_score<5:
        print(" ")
        print(" ")
        print("next round.....")
        option=True
    else:
        if us_score==5:
            print("yahoo!!! You have won the game")
            print(" ")
            print("Do you want to play one more game(y/n): ")
            a=input()
            if a=="y":
                us_score=0
                sy_score=0
                option=True
            else:
                option=False

        else:
            print("Sorry!!! You have lost the game")
            print(" ")
            print("Do you want to play one more game(y/n): ")
            a=input()
            if a=="y":
                us_score=0
                sy_score=0
                option=True
            else:
                option=False