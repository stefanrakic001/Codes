import os


def name():
    name_1 = input("Player_1 please enter your name: ")
    name_2 = input("Player_2 please enter your name: ")
    return name_1, name_2


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


def create_board():
    x = int(input("Mekkora palyat szeretnel? "))
    row = [' '] * x
    cb = []
    for i in range(x):
        cb.append(list(row))

    return cb


def print_board(pb):
    print("#" * (len(pb[0]) * 4 + 1))
    for y in range(len(pb)):
        row_string = "# "
        for x in range(len(pb[y])):
            row_string += str(pb[y][x]) + " # "
        print(row_string)
        print("#" * (len(row_string) - 1))
        

def counter():
    p1 = True
    if p1:
            print(player_1 + ": " + str(len(player1won)))
            print(player_2 + ": " + str(len(player2won)))
            print("Tie: " + str(len(tie)))
        

def player_1_choose(character):
    x = input(player_1 + ',please give number of row and column please separate with a dot: ')
    integer_1 = int(x[0])
    integer_2 = int(x[2])
    p1 = True
    while p1:
        if board[integer_1][integer_2] == ' ':
            board[integer_1][integer_2] = character
            print_board(board)
            os.system("clear")
            p1 = False
            player_2_choose(choice_second[0])
        else:
            print('It is occupied')


def player_2_choose(character):
    print_board(board)
    x = input(player_2 + ',please give number of row and column please separate with a dot: ')
    integer_1 = int(x[0])
    integer_2 = int(x[2])
    p2 = True
    while p2:
        if board[integer_1][integer_2] == ' ':
            board[integer_1][integer_2] = character
            os.system("clear")
            print_board(board)
            p2 = False
            player_1_choose(choice_first[0])
            
        else:
            print('It is occupied')












os.system("clear")

player_1, player_2 = name()

choice_first = []

choice_second = []

character()

print (choice_first, choice_second)

board = create_board()

print_board(board)

player1won = []
player2won = []
tie = []

counter()
player_1_choose(choice_first[0])