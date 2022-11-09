import random
import os
import sys


def get(ship_size=4, dimension = 10):
    if ship_size<dimension:
        return ship_size,dimension
    else:
        print("The ship needs to be smaller than the board, resorting to default inputs: Ship_size:4, Dimensions:10")
        return 4,10


def start_board(ship_size,dimension):
    #initialising our board with appropriate row and column names
    board=[]
    for i in range(dimension+1):
        board_row=[]
        for j in range(dimension+1):
            if j==0:
                if i==0:
                    board_row.append(" ")
                else:
                    board_row.append(i-1)
            elif i==0:
                board_row.append(chr(ord('A')+j-1))
            else:
                board_row.append(" ")
        board.append(board_row)

    #initialising another board where the info of our ship will be stored
    boardx=[]
    for i in range(dimension+1):
        board_rowx=[]
        for j in range(dimension+1):
            if j==0:
                if i==0:
                    board_rowx.append(" ")
                else:
                    board_rowx.append(i-1)
            elif i==0:
                board_rowx.append(chr(ord('A')+j-1))
            else:
                board_rowx.append(" ")
        boardx.append(board_rowx)
    

    #printing our board for the first time, this is the first thing shown when our program is executed
    os.system("clear")
    print("\n"+ " "*(dimension+1)+"Welcome to Battleship!\n ")
    for i in range(dimension+1):
        for j in range(dimension+1):
            if i==0:
                print(str(board[i][j])+"  ",end=" ")
            else:
                print(str(board[i][j])+" |", end=" ")
        print()
        print("  +"+"---+"*dimension)

    return board, boardx

def place_ship(ship_size,dimension,boardx):
    #computer assigns coordinates for the location of our ship using a random function

    x=random.randint(0,1)
    if x==1:
        y=random.randint(1,dimension)
        z=random.randint(1,dimension-ship_size+1)
        for i in range(ship_size):
                boardx[y][z+i]='*'
    else:
        y=random.randint(1,dimension-ship_size+1)
        z=random.randint(1,dimension)
        for i in range(ship_size):
            boardx[y+i][z]="*"

    return boardx


#loop which asks the users for input, checks user's input and prints board after updating it

def play(board,boardx):
    continue_game=0  
    cnt=0            #for counting the total number of tries taken (only unique attempts and attempts with valid inputs are counted)
    strike=0         #counts the total number of correct strikes on ship
    while(continue_game==0):
        game_input=input("\n  Guess the coordinates of the hidden ship (eg.A6):  ")
        guess=list(game_input)
        if len(guess)==2 and ord('A')-1<ord(guess[0])<ord('A')+dimension and guess[1].isdigit() and 0<=int(guess[1])<dimension:
            row_coordinate= int(guess[1])+1
            col_coordinate= ord(guess[0])- ord('A') + 1
            if board[row_coordinate][col_coordinate]=="X" or board[row_coordinate][col_coordinate]=="#":
                print("  This coordinate has been tried previously. Please try again")
                continue;
            if boardx[row_coordinate][col_coordinate]=='*':
                strike=strike+1
                board[row_coordinate][col_coordinate]='X'
            else:
                board[row_coordinate][col_coordinate]='#'
        else:
            print("  Invalid input, please enter the desired coordinate properly")
            continue;
        os.system("clear")
        for i in range(dimension+1):
            for j in range(dimension+1):
                if i==0:
                    print(str(board[i][j])+"  ",end=" ")
                else:
                    print(str(board[i][j])+" |", end=" ")
            print()
            print("  +"+"---+"*dimension)

        cnt=cnt+1
        if strike==ship_size:
            continue_game=1
            print("\n  Congratulations! You Won!\n""  You took "+str(cnt)+" turns to finish the game.")


if __name__ == "__main__":
    ship_size,dimension = get()
    board,boardx = start_board(ship_size,dimension)
    boardx = place_ship(ship_size,dimension,boardx)
    play(board,boardx)
