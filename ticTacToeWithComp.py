'''
This project is a simple Tic-Tac-Toe game that can be played by a person and a computer.
'''
import random

class TicTacToe:
    def __init__(self):
        self.board = [".", ".", ".",
                      ".", ".", ".",
                      ".", ".", "."]
        self.first_player = ""
        self.game_still_on = True
        self.winner = False 
        
    
    def play_game(self):
        self.display_board()
        self.first_to_play()
        while self.game_still_on:
            self.handle_turn(self.first_player)
            self.check_for_winner(self.first_player)
            self.check_for_tie()
            self.flip_player(self.first_player)
            

    def display_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")

    
    def first_to_play(self):
        welcome_note = input("Welcome to Tic-Tac-Toe game. Do you want to play first? \nEnter Y for Yes, N for No: ").upper()
        ready_to_play = True
        while ready_to_play:
            if welcome_note == "N":
                print("\nMy turn")
                computer_play = random.choice([0,1,2,3,4,5,6,7,8])
                self.board[computer_play] = "O"
                self.first_player = "human"
                ready_to_play = False
                self.display_board()
            
            elif welcome_note == "Y":
                self.display_board()
                print("\nYour turn")
                position = input("Select a position from 1 to 9: ")
                valid_selection = [str(x) for x in range(1, len(self.board) + 1)]
                selection = 0
                while position not in valid_selection:
                    position = input("\nInvalid position...!!!\n \nSelect a position from 1 to 9: ")
                selection = int(position) - 1    
                self.board[selection] = "X"
                self.first_player = "computer"
                ready_to_play = False
                self.display_board()     
            
            else:
                self.display_board()
                welcome_note = input("Invalid entry...!!!\n \nDo you want to play first? Enter Y for Yes, N for No: ").upper()
          

    def handle_turn(self, player):
        if player == "human":
            print("\nYour turn")
            position = input("Select a position from 1 to 9: ")
            selection = 0
            empty_position = True
            valid_selection = [str(x) for x in range(1, len(self.board) + 1)]
            while empty_position:
                while position not in valid_selection:
                    position = input("\nInvalid position...!!! \nSelect a position from 1 to 9: ")
                selection = int(position) - 1
                if self.board[selection] != ".":
                    print(f"\nPosition {position} already selected...!!!\n")
                    position = input("Select a position from 1 to 9: ")
                else:
                    empty_position = False
            self.board[selection] = "X"

        if player == "computer":
            print("\nMy turn")
            computer_play = random.choice([0,1,2,3,4,5,6,7,8])
            while self.board[computer_play] != ".":
                computer_play = random.choice([0,1,2,3,4,5,6,7,8])
            self.board[computer_play] = "O"
        self.display_board()


    def check_for_winner(self, player):
        # Rows check
        row_1 = self.board[0] == self.board[1] == self.board[2] != "."
        row_2 = self.board[3] == self.board[4] == self.board[5] != "."
        row_3 = self.board[6] == self.board[7] == self.board[8] != "."

        # Columns check
        column_1 = self.board[0] == self.board[3] == self.board[6] != "."
        column_2 = self.board[1] == self.board[4] == self.board[7] != "."
        column_3 = self.board[2] == self.board[5] == self.board[8] != "."

        # Diagonals check
        diagonal_1  =self.board[0] == self.board[4] == self.board[8] != "."
        diagonal_2 = self.board[2] == self.board[4] == self.board[6] != "."

        # Row winner
        if row_1 or row_2 or row_3:
            if player == "human":
                print("Game Over! \nYou (X) won")
                self.game_still_on = False
                self.winner = True
            if player == "computer":
                print("Game Over! \nYou (X) lost")
                self.game_still_on = False
                self.winner = True

        # Column winner
        elif column_1 or column_2 or column_3:
            if player == "human":
                print("Game Over! \nYou (X) won")
                self.winner = True
                self.game_still_on = False
            if player == "computer":
                print("Game Over! \nYou (X) lost")
                self.winner = True
                self.game_still_on = False
            
    
        # Diagonal winner 
        elif diagonal_1 or diagonal_2:
            if player == "human":
                print("Game Over! \nYou (X) won")
                self.game_still_on = False
                self.winner = True
            if player == "computer":
                print("Game Over! \nYou (X) lost")
                self.game_still_on = False
                self.winner = True
            

    def check_for_tie(self):
        if "." not in self.board and (self.winner == False):
            print("Game Over! \nIt's a tie")
            self.game_still_on = False
       

    def flip_player(self, player):
        if player == "human":
            self.first_player = "computer"
        if player == "computer":
            self.first_player = "human"

  
game=TicTacToe()
game.play_game()       



