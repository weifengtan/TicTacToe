import random
counter = 0 
class Player:
    def __init__(self, name, sign):
        self.name = name # player's name
        self.sign = sign # player's sign O or X
    def get_sign(self):
        # return an instance sign
        sign = self.sign
        return sign
    def get_name(self):
        # return an instance name
        name = self.name
        return name
    def choose(self, board):
        # prompt the use to choose a cell
        # if the user enters a valid string and the cell on the board is empty, update the board
        # otherwise print a message that the input is wrong and rewrite the prompt
        # use the methods board.isempty(cell), and board.set(cell,sign)
        all_moves = ("A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3")

        while True :
            cell =  input((self.name + ", " + self.sign + ": Enter a cell [A-C][1-3]:\n"))
            cell_upper = cell.upper()
            
            if cell_upper in all_moves :
                if board.isempty(cell_upper) == True :
                    board.set(cell_upper, self.sign)
                    break
                else :
                    print("You did not choose correctly.")


# SUBCLASS AI
class AI(Player):
    def __init__(self, name, sign, board):
        self.name = name
        self.sign = sign
        self.moves = list(("A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"))

    def choose(self, board):
        print (self.name + ", " + self.sign + ": Enter a cell [A-C][1-3]:")
        
        while True:
            ai = random.choice(self.moves)
            if board.isempty(ai) == True :
                board.set(ai, self.sign)
                self.moves.remove(ai)
                break
            else :
                print("You did not choose correctly")

            print (ai)

# SUBCLASS SmartAI
class SmartAI(AI):
     def choose(self, board):
        smart_list = list(("A1", "C1", "B2", "A3", "C3"))
        
        
        all_list = list(("A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"))
        #all_list = list(("A1", "B1", "C3"))
        global counter

        if self.sign == "X" :
            opp = "O"
        else:
            opp = "X"
        
        print (self.name + ", " + self.sign + ": Enter a cell [A-C][1-3]:")
                        
        # WINNING THE GAME   
        if board.board[0] == self.sign and  board.board[2] == self.sign and board.board[1] == " " :
            print ("B1")
            board.set("B1", self.sign)
        elif board.board[0] == self.sign and board.board[1] == self.sign and board.board[2] == " " :
            print ("C1")
            board.set("C1", self.sign)
        elif board.board[1] == self.sign and board.board[2] == self.sign and board.board[0] == " " :
            print ("A1")
            board.set("A1", self.sign)
        elif board.board[3] == self.sign and board.board[4] == self.sign and board.board[5] == " ":
            print ("C2")
            board.set("C2", self.sign)
        elif board.board[4] == self.sign and board.board[5] == self.sign and board.board[3] == " ":
            print ("A2")
            board.set("A2", self.sign)
        elif board.board[3] == self.sign and board.board[5] == self.sign and board.board[4] == " ":
            print ("B2")
            board.set("B2", self.sign) 
        elif board.board[6] == self.sign and board.board[7] == self.sign and board.board[8] == " ":
            print ("C3")
            board.set("C3", self.sign)
        elif board.board[7] == self.sign and board.board[8] == self.sign and board.board[6] == " ":
            print ("A3")
            board.set("A3", self.sign)
        elif board.board[6] == self.sign and board.board[8] == self.sign and board.board[7] == " ":
            print ("B3")
            board.set("B3", self.sign)
        elif board.board[0] == self.sign and board.board[3] == self.sign and board.board[6] == " ":
            print ("A3")
            board.set("A3", self.sign)
        elif board.board[3] == self.sign and board.board[6] == self.sign and board.board[0] == " ":
            print ("A1")
            board.set("A1", self.sign)
        elif board.board[0] == self.sign and board.board[6] == self.sign and board.board[3] == " ":
            print ("A2")
            board.set("A2", self.sign)
        elif board.board[1] == self.sign and board.board[4] == self.sign and board.board[7] == " ":
            print ("B3")
            board.set("B3", self.sign)
        elif board.board[4] == self.sign and board.board[7] == self.sign and board.board[1] == " ":
            print ("B1")
            board.set("B1", self.sign)
        elif board.board[1] == self.sign and board.board[7] == self.sign and board.board[4] == " ":
            print ("B2")
            board.set("B2", self.sign)
        elif board.board[2] == self.sign and board.board[5] == self.sign and board.board[8] == " ":
            print ("C3")
            board.set("C3", self.sign)
        elif board.board[5] == self.sign and board.board[8] == self.sign and board.board[2] == " ":
            print ("C1")
            board.set("C1", self.sign)
        elif board.board[2] == self.sign and board.board[8] == self.sign and board.board[5] == " ":
            print ("C2")
            board.set("C2", self.sign)
        elif board.board[0] == self.sign and board.board[4] == self.sign and board.board[8] == '' :
            print ("C3")
            board.set("C3", self.sign)
        elif board.board[4] == self.sign and board.board[8] == self.sign and board.board[0] == " ":
            print ("A1")
            board.set("A1", self.sign)
        elif board.board[0] == self.sign and board.board[8] == self.sign and board.board[4] == '' :
            print ("B2")
            board.set("B2", self.sign)
        elif board.board[2] == self.sign and board.board[4] == self.sign and board.board[6] == " ":
            print ("A3")
            board.set("A3", self.sign)
        elif board.board[4] == self.sign and board.board[6] == self.sign and board.board[2] == " ":
            print ("C1")
            board.set("C1", self.sign)
        elif board.board[2] == self.sign and board.board[6] == self.sign and board.board[4] == " ":
            print ("B2")
            board.set("B2", self.sign)

        # BLOCKING THE OPPONENT
        elif board.board[0] == opp and  board.board[2] == opp and board.board[1] == " " :
            print ("B1")
            board.set("B1", self.sign)
        elif board.board[0] == opp and board.board[1] == opp and board.board[2] == " " :
            print ("C1")
            board.set("C1", self.sign)
        elif board.board[1] == opp and board.board[2] == opp and board.board[0] == " " :
            print ("A1")
            board.set("A1", self.sign)
        elif board.board[3] == opp and board.board[4] == opp and board.board[5] == " ":
            print ("C2")
            board.set("C2", self.sign)
        elif board.board[4] == opp and board.board[5] == opp and board.board[3] == " ":
            print ("A2")
            board.set("A2", self.sign)
        elif board.board[3] == opp and board.board[5] == opp and board.board[4] == " ":
            print ("B2")
            board.set("B2", self.sign) 
        elif board.board[6] == opp and board.board[7] == opp and board.board[8] == " ":
            print ("C3")
            board.set("C3", self.sign)
        elif board.board[7] == opp and board.board[8] == opp and board.board[6] == " ":
            print ("A3")
            board.set("A3", self.sign)
        elif board.board[6] == opp and board.board[8] == opp and board.board[7] == " ":
            print ("B3")
            board.set("B3", self.sign)
        elif board.board[0] == opp and board.board[3] == opp and board.board[6] == " ":
            print ("A3")
            board.set("A3", self.sign)
        elif board.board[3] == opp and board.board[6] == opp and board.board[0] == " ":
            print ("A1")
            board.set("A1", self.sign)
        elif board.board[0] == opp and board.board[6] == opp and board.board[3] == " ":
            print ("A2")
            board.set("A2", self.sign)
        elif board.board[1] == opp and board.board[4] == opp and board.board[7] == " ":
            print ("B3")
            board.set("B3", self.sign)
        elif board.board[4] == opp and board.board[7] == opp and board.board[1] == " ":
            print ("B1")
            board.set("B1", self.sign)
        elif board.board[1] == opp and board.board[7] == opp and board.board[4] == " ":
            print ("B2")
            board.set("B2", self.sign)
        elif board.board[2] == opp and board.board[5] == opp and board.board[8] == " ":
            print ("C3")
            board.set("C3", self.sign)
        elif board.board[5] == opp and board.board[8] == opp and board.board[2] == " ":
            print ("C1")
            board.set("C1", self.sign)
        elif board.board[2] == opp and board.board[8] == opp and board.board[5] == " ":
            print ("C2")
            board.set("C2", self.sign)
        elif board.board[0] == opp and board.board[4] == opp and board.board[8] == '' :
            print ("C3")
            board.set("C3", self.sign)
        elif board.board[4] == opp and board.board[8] == opp and board.board[0] == " ":
            print ("A1")
            board.set("A1", self.sign)
        elif board.board[0] == opp and board.board[8] == opp and board.board[4] == '' :
            print ("B2")
            board.set("B2", self.sign)
        elif board.board[2] == opp and board.board[4] == opp and board.board[6] == " ":
            print ("A3")
            board.set("A3", self.sign)
        elif board.board[4] == opp and board.board[6] == opp and board.board[2] == " ":
            print ("C1")
            board.set("C1", self.sign)
        elif board.board[2] == opp and board.board[6] == opp and board.board[4] == " ":
            print ("B2")
            board.set("B2", self.sign)

        
        
        else :
            while True:
                if board.board[0] != " " and board.board[2] != " " and board.board[6] != " " and board.board[8] != " " :
                    random_all = random.choice(all_list)
                    if board.isempty(random_all) == True :
                        board.set(random_all, self.sign)
                        print (random_all)
                        break
                    else :
                        pass
                    
                random_smart = random.choice(smart_list)
                if board.isempty(random_smart) == True :
                    board.set(random_smart, self.sign)
                    smart_list.remove(random_smart)
                    print (random_smart)
                    break
                else :
                    pass


        
# SUBCLASS MiniMax
class MiniMax(AI):
    def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        cell = MiniMax.minimax(self, board, True, True)
        print(cell)
        board.set(cell, self.sign)
        
    def minimax(self, board, self_player, start):
        if board.isdone():
            if board.get_winner() == self.sign: 
                return 1
            # is a tie
            elif board.get_winner() == "":
                return 0
            # self is a looser (opponent is a winner)
            else:
                return -1
            
        if self.sign == "X" :
            opp = "O"
        else:
            opp = "X"
        
        min_score = float("inf")
        max_score = float("-inf")
        move = ''

        all_cells = list(("A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"))
        
        for i in all_cells:
            if board.isempty(i) :
                if self_player == True :
                    board.set(i, self.sign)
                else :
                    board.set(i, opp)

                score = MiniMax.minimax(self, board, not self_player, False)
                if self_player == True :
                    if score > max_score :
                        max_score = score
                        move = i
                else :
                    if score < min_score :
                        min_score = score

                board.set(i, ' ')

        if start == True :
            return move
        elif self_player == True :
            return max_score
        elif self_player == False:
            return min_score
        
    
    

        

        
        

    
        
    
    
    
    
