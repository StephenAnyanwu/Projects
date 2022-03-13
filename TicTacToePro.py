'''
This project is a Tic-Tac_Toe game of 3 by 3 board for 2 players where each player has 3 identical signs different
from that of the other player (i.e. 3 X's and 3 O's) to be placed on the game board. For a winner to emerge, he has
to place his signs on the same column, row or diagonal of the game board. Note that 3 empty spaces will be left out 
after the players must have placed their individual signs on the game board in turn.
After the placement of the signs and no winner emerged, the players have to be moving their individual signs in turn  
on the game board until either player's signs fall on the same column, row or diagonal thus, a winner emerges.
'''

class TicTacToe_Pro:
    def __init__(self):
        self.board = [".", ".", ".",
                      ".", ".", ".",
                      ".", ".", "."]

        self.game_still_on = True
        self.player = "X"
        self.place_signs = "STAGE 1: Placing signs on the board."
        self.move_signs = "STAGE 2: Moving signs on the board."
        self.stage = self.place_signs
        self.winner = False
       

    def play_game(self):
        # display the Tic-Tac-Toe game borad
        self.display_board()

        # while the game is still going on...
        while self.game_still_on:

            # place sign of an arbitrary player on the game board
            self.placing_sign_on_board(self.player)

            # check if arbitrary player has won while placing the signs on the game board
            self.check_for_winner(self.player)

            # flip player to other player
            self.flip_player(self.player)

        # while no winner yet...
        while self.winner == False:

            # move sign of arbitrary player to get a win
            self.moving_sign_on_board(self.player)

            # check if arbitrary player has won while moving the signs on the game board
            self.check_for_winner(self.player)

            # flip to other player
            self.flip_player(self.player)


    def display_board(self):
        '''
        This method displays the game board.
        '''
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}   -----{self.stage}-----")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")

    
    def placing_sign_on_board(self, player):
        """
        This method duty is to place sign of arbitrary player on the game board in turn.
        """
        # check if empty spaces of the game board is greater than 3
        # note that after all the signs are placed on the board, there will be 3 empty spaces left
        if self.board.count(".") > 3:
            print(f"\n{player}'s turn")
            position = input("Select a position 1 to 9 on the board: ").upper()
            selection = 0
            empty_position = True
            valid_selection = [str(x) for x in range(1, len(self.board) + 1)]
            while empty_position:
                
                while position not in valid_selection:
                    position = input("\nInvalid position...!!!\n\nSelect a position from 1 to 9 on the board: ").upper()
                selection = int(position) - 1
                if self.board[selection] != ".":
                    print(f"\nPosition {position} already selected...!!!")
                    position = input("\nSelect a position from 1 to 9: ")
                else:
                    empty_position = False
            self.board[selection] = player
            self.display_board()


        # check if empty spaces on the game board is equal to 3
        if self.board.count(".") == 3:
            self.stage = self.move_signs
            print("\n----------------------------------------------------------------\nNo winner recorded yet")
            self.display_board()
            self.game_still_on = False
        

    def check_for_winner(self, player):
        '''
        This method checks if arbitrary player has won the game.
        '''
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
            game_over = True

    def flip_player(self, player):
        '''
        This method flips player to another player while playing the game.
        '''
        if player == "X":
            self.player = "O"
        if player == "O":
            self.player = "X"


    def moving_sign_on_board(self, player):
        '''
        This method moves signs of arbitrary player on the game board if there is no winner yet.
        '''
        print(f"\n{player}'s turn")
        valid_selection = [str(x) for x in range(1, len(self.board) + 1)]
        pick_up_position = input(f"Pick up '{player}' by entering its present position number on the board: ")
        correct_pick = True
        selection = 0
        while correct_pick:
            while pick_up_position not in valid_selection:
                 pick_up_position = input(f"\nInvalid '{player}' position pick, position not on the board...!!! \n\nPick up '{player}' by entering its present position number on the board: ")
            selection = int(pick_up_position)-1
            if self.board[selection] != player:
                pick_up_position = input(f"\nInvalid '{player}' picked up...!!! \n\nPick up '{player}' by entering its present position number on the board: ")
            else:
                correct_pick = False
        self.board[selection] = "."

        drop_off_position = input(f"Move '{player}' to new position by entering the new position number on the board: ")
        correct_drop = True
        selection = 0
        while correct_drop:
            while drop_off_position not in valid_selection:
                drop_off_position = input(f"\nInvalid '{player}' move, position not on the board...!!! \n\nMove '{player}' to new position by entering the new position number on the board:  ")    
            selection = int(drop_off_position) - 1
            if self.board[selection] != ".":
                drop_off_position = input(f"\nInvalid '{player}' move, position already taken...!!! \n\nMove '{player}' to new position by entering the new position number on the board: ")
            elif drop_off_position == pick_up_position:
                drop_off_position = input(f"\nInvalid '{player}' move, pick up position equals drop off position..!!! \n\nMove '{player}' to new position by entering the new position number on the board: ")
            else:
                correct_drop = False
        self.board[selection] = player
        self.display_board()


# play Tic-Tac-Toe game            
TicTacToe_Pro().play_game()

# restart Tic-Tac-Toe game if there is a winner
play_again = True
restart = input("\nDo you want to restart? Enter Y for Yes, N for No: ").upper()
while play_again:
    if restart == "N":
        play_again = False
    elif restart == "Y":
        TicTacToe_Pro().play_game()
        restart = input("\nDo you want to restart? Enter Y for Yes, N for No: ").upper()
    else:
        print("\nInvalid Entry...!!!")
        restart = input("\nDo you want to restart the game? Enter Y for Yes, N for No: ").upper()



    

