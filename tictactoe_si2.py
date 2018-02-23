import os


def current_score(filename):
    player_score = open(filename, 'w')
    player_score.write(str(len(player_1_won)) + '\n')
    player_score.write(str(len(player_2_won)) + '\n')
    player_score.write(str(len(tie)))
    player_score.close()


def load_score():
    file = open('score.txt', 'r')
    cont = file.readlines()
    for i in range(int(cont[0][0])):
        player_1_won.append("w")
    for i in range(int(cont[1][0])):
        player_2_won.append("w")
    for i in range(int(cont[2][0])):
        tie.append('w')
        file.close()


def save():
    while True:
        a = input('Do you want to save the score?')
        if a == 's':
            current_score('score.txt')
    
            break


def load():
    a = input('Do you want to load a game?--> y ')
    if a == 'y':
        load_score()


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
            print(player_1 + ": " + str(len(player_1_won)))
            print(player_2 + ": " + str(len(player_2_won)))
            print("Tie: " + str(len(tie)))
        

def player_1_choose(character):
    occu = True
    while occu:
        if check_win(choice_first[0]):
            return False
        elif check_win(choice_second[0]):
            return False
        else:
            x = input(player_1 + ' ,please give number of row and column please separate with a dot: ')
            integer_1 = int(x[0])
            integer_2 = int(x[2])
            if board[integer_1][integer_2] == ' ':
                board[integer_1][integer_2] = character
                os.system("clear")
                print_board(board)
                occu = False
            else:
                print('It is occupied')


def player_2_choose(character):
    occu = True
    while occu:
        if check_win(choice_second[0]):
            return False
        elif check_win(choice_first[0]):
            return False
        else:
            x = input(player_2 + ' ,please give number of row and column please separate with a dot: ')
            integer_1 = int(x[0])
            integer_2 = int(x[2])
            if board[integer_1][integer_2] == ' ':
                board[integer_1][integer_2] = character
                os.system("clear")
                print_board(board)
                occu = False
            else:
                print('It is occupied')


def check_win(a):
    char = a
    for i in range(len(board)):
            for j in range(len(board[i])):
                try: 
                    if 0 < j < len(board) - 1:
                        if board[i][j - 1] == char and board[i][j + 1] == char: #balra-jobbra
                            return True
                except IndexError:
                    pass
                try:
                    if i > 0 and i < len(board) - 1 and j > 0 and j < len(board) - 1:
                        if board[i - 1][j - 1] == char and board[i + 1][j + 1] == char: #balrafol-jobbrale
                            return True
                except IndexError:
                    pass
                try:
                    if i > 0 and i < len(board) - 1 and j > 0 and j < len(board) - 1:
                        if board[i - 1][j + 1] == char and board[i + 1][j - 1] == char: #jobbfölballe
                            return True
                except IndexError:
                    pass
                try:
                    if 0 < i < len(board) - 1:
                        if board[i + 1][j] == char and board[i - 1][j] == char: #fol-le
                            return True
                except IndexError:
                    pass
    return False
        

os.system("clear")

player_1_won = []
player_2_won = []
tie = []

load()

player_1, player_2 = name()

choice_first = []

choice_second = []

character()

board = create_board()

print_board(board)


counter()


while True:
    result = player_1_choose(choice_first[0])
    if result is False:
        print(player_1 + " you win!")
        player_1_won.append("W")
        counter()
        save()
        break
    result = player_2_choose(choice_second[0])
    if result is False:
        print(player_2 + " you win!")
        player_2_won.append("W")
        counter()
        save()
        break

