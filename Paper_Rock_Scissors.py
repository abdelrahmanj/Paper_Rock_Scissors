
options = ["r", "p", "s"]

import random

while True:
     

    User = input("What's your choice?  'r for rock, p for paper,  s for sessior' \n").lower()


    PC = random.choice(options)

    

    if User not in options:
        print("Invalid Choice. Please try again.")
        continue

    print(f"You played {User}")
    print(f"PC played {PC}")

   

    if User == PC:
        print("It's a tie")

    elif (User == "s" and PC == "p") or (User == "r" and PC == "s") or ( User == "p" and PC == "r"):
            print("You Won!")   
    else:
        print("You Lost")  

    play_again = input("Do you want to play again? (y/n): ").lower()
    
    while  play_again not in ["y", "n"]:
        print("Invalid choice. Please enter y/n")
        play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        break



     
    


