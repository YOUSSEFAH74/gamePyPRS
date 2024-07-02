import random
choices = ['rock', 'paper', 'scissors']
Ai = random.choice(choices)
player = None
while player not in choices:
    player =  input("rock, paper or scissors?:").lower()
    print('-' * 50)
if player == Ai:
    print("computer:",Ai)
    print('-' * 50)
    print("player:",player)
    print('-' * 50)
    print("Tie!")
    print('-' * 50)
elif player == "rock":
    if Ai == 'paper':
        print("computer:",Ai)
        print('-' * 50)
        print("player:",player)
        print('-' * 50)
        print("You lose!")
    if Ai == 'scissors':
        print("computer:",Ai)
        print('-' * 50)
        print("player:",player)
        print('-' * 50)
        print("You Win!")
elif player == "scissors":
    if Ai == 'rock':
        print("computer:",Ai)
        print('-' * 50)
        print("player:",player)
        print('-' * 50)
        print("You lose!")
    if Ai == 'paper':
        print("computer:",Ai)
        print('-' * 50)
        print("player:",player)
        print('-' * 50)
        print("You Win!")
elif player == "paper":
    if Ai == 'scissors':
        print("computer:",Ai)
        print('-' * 50)
        print("player:",player)
        print('-' * 50)
        print("You lose!")
    if Ai == 'rock':
        print("computer:",Ai)
        print('-' * 50)
        print("player:",player)
        print('-' * 50)
        print("You Win!")
    
        
    
    

