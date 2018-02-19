import os

# def save_program(file_name):
#     if save1 = 's':
#         save =open(file_name, 'w')
#         for 


def start_program():
    program = True
    return program


def stop_program():
    program = False
    return program


def print_board():
    print("#######################################")
    print("#            #            #           #")
    print("#            #            #           #")
    print("#    ", board[6], "     #     ", board[7], "    #    ", board[8], "    #")
    print("#            #            #           #")
    print("#            #            #           #")
    print("#######################################")
    print("#            #            #           #")
    print("#            #            #           #")
    print("#    ", board[3], "     #     ", board[4], "    #    ", board[5], "    #")
    print("#            #            #           #")
    print("#            #            #           #")
    print("#######################################")
    print("#            #            #           #")
    print("#            #            #           #")
    print("#    ", board[0], "     #     ", board[1], "    #    ", board[2], "    #")
    print("#            #            #           #")
    print("#            #            #           #")
    print("#######################################")


def name():
    name_1 = input("Player_1 please enter your name: ")
    name_2 = input("Player_2 please enter your name: ")
    return name_1, name_2


def character():
    char = True
    while char:
        char = input(player1 + " please choose beetween these characters --> [X/O] ")
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


def check_if_win_1():
    if 7 in player_1 and 4 in player_1 and 1 in player_1:
        print("Congratulations " + player1 + " you win!!!")
        player_1_won.append("W")
        program = False
        return True
    if 8 in player_1 and 5 in player_1 and 2 in player_1:
        print("Congratulations " + player1 + " you win!!!")
        player_1_won.append("W")
        program = False
        return True
    if 9 in player_1 and 6 in player_1 and 3 in player_1:
        print("Congratulations " + player1 + " you win!!!")
        player_1_won.append("W")
        program = False
        return True
    if 1 in player_1 and 2 in player_1 and 3 in player_1:
        print("Congratulations " + player1 + " you win!!!")
        player_1_won.append("W")
        program = False
        return True
    if 4 in player_1 and 5 in player_1 and 6 in player_1:
        print("Congratulations " + player1 + " you win!!!")
        player_1_won.append("W")
        program = False
        return True
    if 7 in player_1 and 8 in player_1 and 9 in player_1:
        print("Congratulations " + player1 + " you win!!!")
        player_1_won.append("W")
        program = False
        return True
    if 1 in player_1 and 5 in player_1 and 9 in player_1:
        print("Congratulations " + player1 + " you win!!!")
        player_1_won.append("W")
        program = False
        return True
    if 7 in player_1 and 5 in player_1 and 3 in player_1:
        print("Congratulations " + player1 + " you win!!!")
        player_1_won.append("W")
        program = False
        return True
    if len(player_1) == 5:
        print("The score is Tie")
        tie.append("T")
        program = False
        return True
    return False


def check_if_win_2():
    if 7 in player_2 and 4 in player_2 and 1 in player_2:
        print("Congratulations " + player2 + " you win!!!")
        player_2_won.append("W")
        program = False
        return True
    if 8 in player_2 and 5 in player_2 and 2 in player_2:
        print("Congratulations " + player2 + " you win!!!")
        player_2_won.append("W")
        program = False
        return True
    if 9 in player_2 and 6 in player_2 and 3 in player_2:
        print("Congratulations " + player2 + " you win!!!")
        player_2_won.append("W")
        program = False
        return True
    if 1 in player_2 and 2 in player_2 and 3 in player_2:
        print("Congratulations " + player2 + " you win!!!")
        player_2_won.append("W")
        program = False
        return True
    if 4 in player_2 and 5 in player_2 and 6 in player_2:
        print("Congratulations " + player2 + " you win!!!")
        player_2_won.append("W")
        program = False
        return True
    if 7 in player_2 and 8 in player_2 and 9 in player_2:
        print("Congratulations " + player2 + " you win!!!")
        player_2_won.append("W")
        program = False
        return True
    if 1 in player_2 and 5 in player_2 and 9 in player_2:
        print("Congratulations " + player2 + " you win!!!")
        player_2_won.append("W")
        program = False
        return True
    if 7 in player_2 and 5 in player_2 and 3 in player_2:
        print("Congratulations " + player2 + " you win!!!")
        player_2_won.append("W")
        program = False
        return True
    if len(player_2) == 5:
        print("The score is Tie")
        tie.append("T")
        program = False
        return True
    return False


def game():
    for i in range(5):
        if i >= 3:
            check_if_win_1()
            check_if_win_2()
        if i == 0:
            print_board()
        p1 = True
        p2 = True
        if (len(player_1_won)) > (len(player_2_won)) and i == 0:
            p1 = False
        if p1:
            print(player1 + ": " + str(len(player_1_won)))
            print(player2 + ": " + str(len(player_2_won)))
            print("Tie: " + str(len(tie)))
        while p1:
            bad_character = True
            
            while bad_character:
                try:
                    x = int(input(player1 + " please choose a field with numpad: "))
                    bad_character = False
                except Exception as e:
                    print("Wrong Character")
            
            if 0 < x < 11 and board[x-1] != "X" and board[x-1] != "O":
                player_1.append(board[x-1])
                board[x-1] = choice_first[0]
                os.system("clear")
                print_board()
                p1 = False
                bad_character = False
                p2 = True
            elif x > 11:
                print("Too high!")
            else:
                print("Field is occupied, please choose another one!")
        if check_if_win_1():
            break
        elif check_if_win_2():
            break
        if p2:
            print(player1 + ": " + str(len(player_1_won)))
            print(player2 + ": " + str(len(player_2_won)))
            print("Tie: " + str(len(tie)))
        while p2:
            badcharacter_2 = True
            
            while badcharacter_2:
                try:
                    x = int(input(player2 + " please choose a field with numpad: "))
                    badcharacter_2 = False
                except Exception as e:
                    print("Wrong Character")

            if 0 < x < 11 and board[x-1] != "X" and board[x-1] != "O":
                player_2.append(board[x-1])
                board[x-1] = choice_second[0]
                os.system("clear")
                print_board()
                p2 = False
                badcharacter_2 = False
                p1 = True
            elif x > 11:
                print("Too high!")
            else:
                print("Field is occupied, please choose another one!")
        if check_if_win_2():
            break
        elif check_if_win_1():
            break


os.system("clear")

player_1_won = []

player_2_won = []

tie = []

player1, player2 = name()

choice_first = []
choice_second = []

character()

program = start_program()

while program:
    if player_1_won == [] and player_2_won == [] and tie == []:
        os.system("clear")
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        player_1 = []
        player_2 = []
        game()
    elif player_1_won != [] or player_2_won != [] or tie != []:
        x = input("Do you want to play again?-->[yes] or [no]")
        if x == "yes":
            os.system("clear")
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            player_1 = []
            player_2 = []
            game()
        elif x == "no":
            stop_program()
            break
        else:
            print("Wrong Input")
    


    