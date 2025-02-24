import random

user_wins = 0 
computer_wins= 0 
options = ["rock", "paper", "scissors"]
options[0]

while True: 
    user_input= input("Type Rock/Paper/Scosspr pr Q tp quit.").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    # rock : 0, paper :1 and scissors: 2 
    computer_picked = options[random_number]
    print("Computer picked", computer_wins + ".")
    
    if user_input == "rock" and computer_picked == "scissors":
        print("You won!")
        user_wins += 1 
        continue
    
    
print("Goodbye!")    