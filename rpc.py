import random 

def start_game():
    user_input = input("'r' for rock, 'p' for paper and 's' for scissor : ")
    
    if user_input != 'r' and user_input != 'p' and user_input != 's' :
        print("invalid input!")
    else :
        guess_lst = ['r', 's', 'p']
        comp_input = random.choice(guess_lst)
        
        print(f"Yours     : {user_input} and\nComputers : {comp_input}\n")
        
        if user_input == comp_input :
            print("tie!")
            start_game()
        elif ( (user_input == 'r' and comp_input == 's') or (user_input == 's' and comp_input == 'p') or (user_input == 'p' and comp_input == 'r') ) :
            print("you win!")
        else :
            print("Computer Win!")

    another_game = input("Do you wanna play again? (y/n) : ")
    if(another_game == 'y'):
        start_game()
    else:
        exit(0)
        
start_game()
