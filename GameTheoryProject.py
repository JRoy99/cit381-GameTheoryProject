import random

def userTurn(stones_list):
    choice1 = False
    choice2 = False
    while not(choice1 and choice2):
        choice1 = False
        choice2 = False
        print(str(stones_list))
        pile_select = int(input("Which pile of stones would you like to take from? "))
        if pile_select > 0 and pile_select < 4:
            choice1 = True
        else:
            print("\nYou must select a valid pile (1 to 3).")
            continue

        stones_removed = int(input("How many stones do you want to remove? "))
    
        if stones_removed > 3 or stones_removed < 1:
            print( "\nYou may only remove 1 to 3 stones per turn.\n")     
        elif stones_list[pile_select-1] - stones_removed < 0:
            print("\nNot enough stones in pile.\n") 
        else:
            choice2 = True
            stones_list[pile_select-1] -= stones_removed
            print( "\nYou removed " + str(stones_removed) + 
                " stone(s) from pile " + str(pile_select) + "! The current stone count is: " + str(stones_list)) 
    
    return stones_list


def aiTurn(stones_list, ai_selection):

    if ai_selection == "Random":
        choice = False

        while not(choice):
            pile_select = random.randint(0,2)
            if stones_list[pile_select] != 0:
                stones_removed = random.randint(1, min(3, stones_list[pile_select]) ) #Take smaller value between 3 and the stones that are left
                choice = True
    
    elif ai_selection == "Optimal":
        modulo_list = []

        for i in range(len(stones_list)):
            modulo_list.append(stones_list[i] % 4)

        if modulo_list[0] > 1 or modulo_list[1] > 1 or modulo_list[2] > 1:
            choice = False
            while not(choice):
                pile_select = random.randint(0,2)
                if modulo_list[pile_select] > 1:
                    stones_removed = modulo_list[pile_select] - 1
                    choice = True
            
        elif sum(modulo_list) == 0:
            choice = False
            while not(choice):
                pile_select = random.randint(0,2)
                if stones_list[pile_select] != 0:
                    stones_removed = 3
                    choice = True

        else:
            choice = False
            while not(choice):
                pile_select = random.randint(0,2)
                if stones_list[pile_select] != 0:
                    stones_removed = 1
                    choice = True

    stones_list[pile_select] -= stones_removed
    print( "\nThe A.I. removed " + str(stones_removed) + 
            " stone(s) from pile " + str(pile_select + 1) + "! The current stone count is: " + str(stones_list) + "\n")

    return stones_list


def main():
    stones_list = [random.randint(5, 10), random.randint(5, 10), random.randint(5, 10)]
    in_game = True

    print("This is a game where players take turns taking 1 to 3 stones from a pile of stones. " +
        "The player who takes the last stone loses.\n" +
        "The current stone count is: ", stones_list, "\n")
    

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
        stones_list = userTurn(stones_list)
        if sum(stones_list) == 0:
            print("You took the last stone, you lost. The A.I. won the game!\n")
            quit()
        stones_list = aiTurn(stones_list, ai_selection)
        if sum(stones_list) == 0:
            print("The A.I took the last stone, it lost. You won the game!")
            quit()

main()