'''
This project is a simple Tic-Tac-Toe game that can be played by two people.
'''

class TicTacToe:
    def __init__(self):
        self.board = [".", ".", ".",
                      ".", ".", ".",
                      ".", ".", "."]
        self.game_still_on = True
        self.player = "X"
        self.winner = False
       
    def play_game(self):
        # display board
        self.display_board()

        # while the game is on...
        while self.game_still_on:
            # handle turn a turn of an arbitrary player
            self.handle_turn(self.player)

            # check if there is a winner
            self.check_for_winner(self.player)

            # check if the game is a tie 
            self.check_for_tie()

             # flip player to other player
            self.flip_player(self.player)
    

    def display_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")


    def handle_turn(self, player):
        print(f"\n{player}'s turn")
        position = input("Select a position from 1 to 9: ")
        selection = 0
        empty_position = True
        valid_selection = [str(x) for x in range(1, len(self.board) + 1)]
        while empty_position:
            while position not in valid_selection:
                position = input("\nInvalid position...!!!\n\nSelect a position from 1 to 9: ")
            selection = int(position) - 1
            if self.board[selection] != ".":
                print(f"\nPosition {position} already selected...!!!")
                position = input("\nSelect a position from 1 to 9: ")
            else:
                empty_position = False
        self.board[selection] = player
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
        diagonal_1 = self.board[0] == self.board[4] == self.board[8] != "."
        diagonal_2 = self.board[2] == self.board[4] == self.board[6] != "."

        # Row winner
        if row_1 or row_2 or row_3:
            print(f"Game Over! \n{player} has won")
            self.game_still_on = False
            self.winner = True

        # Column winner
        elif column_1 or column_2 or column_3:
            print(f"Game Over! \n{player} has won")
            self.game_still_on = False 
            self.winner = True

        # Diagonal winner 
        elif diagonal_1 or diagonal_2:
            print(f"Game Over! \n{player} has won")
            self.game_still_on = False
            self.winner = True


    def check_for_tie(self):
        if "." not in self.board and self.winner==False:
            print("Game Over! \nIt's a tie")
            self.game_still_on = False
        

    def flip_player(self, player):
        if player == "X":
            self.player = "O"
        if player == "O":
            self.player = "X"

game=TicTacToe()
game.play_game()