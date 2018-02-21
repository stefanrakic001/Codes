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
    cb = []
    for i in range(x):
        a = [0] * x
        table = [a] * x
        cb.append(table)
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
        

def navigation():
    p1 = True
    while p1:
        if p1:
            x = input(player_1 + 'Give number of row and column please separate with a dot: ')
            integer_1 = int(x[0])
            integer_2 = int(x[2])
            board[integer_1][integer_2] = 'x'
            print_board(board)










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

navigation()
    