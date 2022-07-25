class Board:
    def __init__(self):
        # board is a list of cells that are represented
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        # the winner's sign O or X
        self.winner = ""
    def get_size(self):
        # optional, return the board size (an instance size)
        size = self.size
        return  size
    
    def get_winner(self):
        # return the winner's sign O or X (an instance winner)
        winner = self.winner
        return winner
    
    def set(self, cell, sign):
        # mark the cell on the board with the sign X or O
        # you need to conver A1, B1 ..., C3 cells into index values fron 1 to 9
        # you can use a tuple ("A1", "B1",...) to obtain indexes
        # this implementation is up to you
        cells = ("A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3")
        self.board[cells.index(cell)] = sign 
                
    def isempty(self, cell):
        # you need to conver A1, B1, ..., C3 cells into index values from 1 to 9
        # return True if the cell is empty (not marked with X or O)
        cells = ("A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3")
        if self.board[cells.index(cell)] == " " :
            return True
        else :
            return False
        
    def isdone(self):
        done = False
        self.winner = ''
        # check all game terminating conditions, if one of them is presentm assign the var done to True
        # depending on consitions assign the instance var winner to O or X
        
        # FIRST GROUP OF IF STATEMENTS ARE FOR COLOMNS 
        if self.board[0] == self.board[3] == self.board[6] :
            if (self.board[0] != " " and self.board[3] != " ") and (self.board[6] != " ") :
                self.winner = self.board[0]
                done = True
                
        elif self.board[1] == self.board[4] == self.board[7] :
            if (self.board[1] != " " and self.board[4] != " ") and (self.board[7] != " ") :
                self.winner = self.board[1]
                done = True
                
        elif self.board[2] == self.board[5] == self.board[8] :
            if (self.board[2] != " " and self.board[5] != " ") and (self.board[8] != " ") :
                self.winner = self.board[2]
                done = True
                
        # SECOND GROUP OF IF STATEMENTS ARE FOR ROWS 
        elif self.board[0] == self.board[1] == self.board[2] :
            if (self.board[0] != " " and self.board[1] != " ") and (self.board[2] != " ") :
                self.winner = self.board[0]
                done = True
                
        elif self.board[3] == self.board[4] == self.board[5] :
            if (self.board[3] != " " and self.board[4] != " ") and (self.board[5] != " ") :
                self.winner = self.board[3]
                done = True
                
        elif self.board[6] == self.board[7] == self.board[8] :
            if (self.board[6] != " " and self.board[7] != " ") and (self.board[8] != " ") :
                self.winner = self.board[6]
                done = True
                
        # THIRD GROUP OF IF STATEMENTS ARE FOR DIAGONALS 
        elif self.board[0] == self.board[4] == self.board[8] :
            if (self.board[0] != " " and self.board[4] != " ") and (self.board[8] != " ") :
                self.winner = self.board[0]
                done = True
                
        elif self.board[2] == self.board[4] == self.board[6] :
            if (self.board[2] != " " and self.board[4] != " ") and (self.board[6] != " ") :
                self.winner = self.board[2]
                done = True
                
        else :
            counter = 0 
            for i in range (0,9):
                if self.board[i] != " " :
                    counter += 1 
                else :
                    done = False

            if counter == 9 :
                done = True
                
            
        return done

    def show(self):
        # draw the board

        # NAMING ALL CELLS SO ITS EASIER TO SEE INSIDE THE FORMAT FOR PRINT STATEMENTS 
        zero = self.board[0]
        one = self.board[1]
        two = self.board[2]
        three = self.board[3]
        four = self.board[4]
        five = self.board[5]
        six = self.board[6]
        seven = self.board[7]
        eight = self.board[8]

        # PRINT OUR THE BOARD
        print ("   A   B   C  ")
        print (" +---+---+---+")
        print ("1| " + zero + " | " + one + " | " + two + " |")
        print (" +---+---+---+")
        print ("2| " + three + " | " + four + " | " + five + " |")
        print (" +---+---+---+")
        print ("3| " + six + " | " + seven + " | " + eight + " |")
        print (" +---+---+---+")
        

        

        
        
        
        
        
