import random

dice = input("Would you like to roll the dice (y = yes) (n = no) : ")

if dice not in ['y','n']:
    print("Invalid Responce")
elif dice == "y":
    while True:
        while dice == 'y':
            num = random.randint(1,6)
            if num == 1:
                print("[---]",sep="\n")
                print("[   ]",sep="\n")
                print("[ 0 ]",sep="\n")
                print("[   ]",sep="\n")
                print("[---]",sep="\n")
                break
            elif num == 2:
                print("[---]",sep="\n")
                print("[  0]",sep="\n")
                print("[   ]",sep="\n")
                print("[0  ]",sep="\n")
                print("[---]",sep="\n")
                break
            elif num == 3:
                print("[---]",sep="\n")
                print("[0  ]",sep="\n")
                print("[ 0 ]",sep="\n")
                print("[  0]",sep="\n")
                print("[---]",sep="\n")
                break
            elif num == 4:
                print("[---]",sep="\n")
                print("[0 0]",sep="\n")
                print("[   ]",sep="\n")
                print("[0 0]",sep="\n")
                print("[---]",sep="\n")
                break
            elif num == 5:
                print("[---]",sep="\n")
                print("[0 0]",sep="\n")
                print("[ 0 ]",sep="\n")
                print("[0 0]",sep="\n")
                print("[---]",sep="\n")
                break
            elif num == 6:
                print("[---]",sep="\n")
                print("[0 0]",sep="\n")
                print("[0 0]",sep="\n")
                print("[0 0]",sep="\n")
                print("[---]",sep="\n")
                break
        dice = input("Would you like to roll the dice again (y = yes) (n = no) : ")
        if dice == "n":
            print("Thank you...Come again")
            break        
        elif dice not in ["y","n"]:
            print("Invalid Responce")
elif dice == "n":
    print("Thank you...Come again")
            