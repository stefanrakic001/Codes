def name():
    name_1 = input("Player_1 please enter your name: ")
    name_2 = input("Player_2 please enter your name: ")
    return name_1, name_2



player_1, player_2 = name()
choice_first = []
choice_second = []

def character():
    char = True
    while char:
        char = input(player_1 + " please choose beetween these characters --> [X/O] ")
        if char == "x":
            choice_first.append("X")
            choice_second.append("O")
            char = False
        elif char == "o":
            choice_first.append("O")
            choice_second.append("X")
            char = False
        else:
            print("Wrong input, please choose beetween these characters --> [X/O]  ")

character()

print (choice_first, choice_second)