
# date: April 14, 2022
# file: tictac.py a Python program that implements a tic-tac-toe game
# input: user responses (strings)
# output: interactive text messages and a tic-tac-toe board

from board import Board
from player import Player, AI, MiniMax

# main program
print("Welcome to TIC-TAC-TOE Game!")
while True:
    board = Board()
    name1 = input ("Player 1 please Enter your name: ")
    name2 = input("Player 2 please enter your name: ") 
    gameMode = input("Select Game Mode (MiniMax, AI, Player): ")
    gameMode = gameMode.upper()
    
    if (gameMode == "MINIMAX"):
        player1 = Player(name1, "X")
        player2 = MiniMax(name2, "O", board)
    elif (gameMode == "AI"):
        player1 = Player(name1, "X")
        player2 = AI(name2, "O", board)
    elif (gameMode == "PLAYER"):
        player1 = Player(name1, "X")
        player2 = Player(name2, "O")
        
    turn = True
    while True:
        board.show()
        if turn:
            player1.choose(board)
            turn = False
        else:
            player2.choose(board)
            turn = True
        if board.isdone():
            break
    board.show()
    if board.get_winner() == player1.get_sign():
        print(f"{player1.get_name()} is a winner!")
    elif board.get_winner() == player2.get_sign():
        print(f"{player2.get_name()} is a winner!")
    else:
        print("It is a tie!")
    ans = input("Would you like to play again? [Y/N]\n").upper()
    if (ans != "Y"):
        break
print("Goodbye!")
