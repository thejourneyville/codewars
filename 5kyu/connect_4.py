"""
Task
The game consists of a grid (7 columns and 6 rows) and two players that take turns to drop their discs. 
The pieces fall straight down, occupying the next available space within the column. 
The objective of the game is to be the first to form a horizontal, vertical, 
or diagonal line of four of one's own discs.

Your task is to create a Class called Connect4 that has a method called play which takes one argument 
for the column where the player is going to place their disc.

Rules
If a player successfully has 4 discs horizontally, vertically or diagonally 
then you should return "Player n wins!” where n is the current player either 1 or 2.

If a player attempts to place a disc in a column that is full 
then you should return ”Column full!” and the next move must be taken by the same player.

If the game has been won by a player, any following moves should return ”Game has finished!”.

Any other move should return ”Player n has a turn” where n is the current player either 1 or 2.
 
Player 1 starts the game every time and alternates with player 2.

The columns are numbered 0-6 left to right.
"""

import random

class Connect4():

    def __init__(self):
        self.board = [[" " for c in range (7)] for r in range (6)]
        self.stacks = {col: 6 for col in range(7)}  # column : height of stack (6 is empty, 0 is full) 
        self.winner = False
        self.current_player = "1"

    def play(self, col):
        
        if self.winner:
            return "Game has finished!"
        
        # adjusts the stack of each column and places the piece on the top of the stack
        if self.stacks[col] > 0:
            self.stacks[col] -= 1
            self.board[self.stacks[col]][col] = self.current_player

        else:
            return "Column full!"
        
        # iterates through 2D array looking for "1" or "2"s
        for current_row in range(6):
            for current_col in range(7):

                if self.board[current_row][current_col].isdecimal():
                    
                    # now checking for 4 in a row in all directions
                    
                    # horzes
                    if current_col <= 3:
                        if len(set([self.board[current_row][current_col],
                                self.board[current_row][current_col + 1],
                                self.board[current_row][current_col + 2],
                                self.board[current_row][current_col + 3]])) == 1:
                            self.winner = True
                    elif current_col >= 3:
                        if len(set([self.board[current_row][current_col],
                                self.board[current_row][current_col - 1],
                                self.board[current_row][current_col - 2],
                                self.board[current_row][current_col - 3]])) == 1:
                            self.winner = True

                    # verts
                    if current_row <= 2:
                        if len(set([self.board[current_row][current_col],
                                self.board[current_row + 1][current_col],
                                self.board[current_row + 2][current_col],
                                self.board[current_row + 3][current_col]])) == 1:
                            self.winner = True
                    elif current_row >= 3:
                        if len(set([self.board[current_row][current_col],
                                self.board[current_row - 1][current_col],
                                self.board[current_row - 2][current_col],
                                self.board[current_row - 3][current_col]])) == 1:
                            self.winner = True

                    # diags
                    # down_right
                    if current_col <= 3 and current_row <= 2:
                        if len(set([self.board[current_row][current_col], 
                                self.board[current_row + 1][current_col + 1], 
                                self.board[current_row + 2][current_col + 2], 
                                self.board[current_row + 3][current_col + 3]])) == 1:
                            self.winner = True

                    # down_left
                    if current_col >= 3 and current_row <= 2:
                        if len(set([self.board[current_row][current_col], 
                                self.board[current_row + 1][current_col - 1], 
                                self.board[current_row + 2][current_col - 2], 
                                self.board[current_row + 3][current_col - 3]])) == 1:
                            self.winner = True
                    
                    # up_right
                    if current_col <= 3 and current_row >= 3:
                        if len(set([self.board[current_row][current_col], 
                                self.board[current_row - 1][current_col + 1], 
                                self.board[current_row - 2][current_col + 2], 
                                self.board[current_row - 3][current_col + 3]])) == 1:
                            self.winner = True
                    
                    # up_left
                    if current_col >= 3 and current_row >= 3:
                        if len(set([self.board[current_row][current_col], 
                                self.board[current_row - 1][current_col - 1], 
                                self.board[current_row - 2][current_col - 2], 
                                self.board[current_row - 3][current_col - 3]])) == 1:
                            self.winner = True
        
        # alternates the player
        if not self.winner:
            if self.current_player == "1":
                self.current_player = "2"
                return "Player 1 has a turn"
            else:
                self.current_player = "1"
                return "Player 2 has a turn"               
        else:
            return f"Player {self.current_player} wins!"

# below is for testing using the random module to chose which column to drop into
game = Connect4()

while True:
    
    select_col = random.randint(0, 6)
    print(game.play(select_col))
    b = game.board
    for row in b:
        print(row)
    input("press enter")
