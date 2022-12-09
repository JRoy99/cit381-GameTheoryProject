import random

def userTurn(stones_left):
    stones_removed = int(input("How many stones do you want to remove? "))
    
    if stones_removed > 3 or stones_removed < 1:
        print( "\nYou must remove 1 to 3 stones per turn!\n The current stone count is: " + str(stones_left) )     
    elif stones_left - stones_removed < 0:
        print("\nThere aren't that many stones left!\n") #Give user error!  
    else:
        stones_left -= stones_removed
        print( "\nYou removed " + str(stones_removed) + 
            " stone(s)! The current stone count is: " + str(stones_left)) 
    return stones_left


def aiTurn(stones_left, ai_selection):

    if ai_selection == "Random":
        stones_removed = random.randint(1, min(3, stones_left) ) #Take smaller value between 3 and the stones that are left
    
    elif ai_selection == "Optimal":
        if stones_left % 4 == 0:
            next_lowest_factor = stones_left - 4
        else:
            next_lowest_factor = int(stones_left / 4) * 4
        
        stones_removed = max(1, stones_left - (next_lowest_factor + 1))
        if stones_removed > 3:
            random.randint(1, 3)

    stones_left -= stones_removed
    print( "\nThe A.I. removed " + str(stones_removed) + 
            " stone(s)! The current stone count is: " + str(stones_left) + "\n")

    return stones_left


def main():
    stones_left = random.randint(15, 30)
    in_game = True

    print("This is a game where players take turns taking 1 to 3 stones from a pile of stones." +
        "The player who takes the last stone loses.\n" +
        "The current stone count is: ", stones_left, "\n")
    

    choice = True
    while choice:
        ai_choice = str(input("Play against a {R}andom or {O}ptimal CPU? "))
        if ai_choice.lower() == 'r':
            ai_selection = "Random"
            choice = False
        elif ai_choice.lower() == 'o':
            ai_selection = "Optimal"
            choice = False               


    while in_game:
        stones_left = userTurn(stones_left)
        if stones_left == 0:
            print("You took the last stone, you lost. The A.I. won the game!\n")
            quit()
        stones_left = aiTurn(stones_left, ai_selection)
        if stones_left == 0:
            print("The A.I took the last stone, it lost. You won the game!")
            quit()

main()