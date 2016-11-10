# ID#43351454
import piece
import board
import rules
import search


class Input:

    def get_init_row(self) -> int:
        "get initialize row from user input"
        while True:
            row = int(input(""))
            if row >= 4 and row <=16 and row%2 == 0:
                return row
            else:
                print("invalid row input")
            
    def get_init_col(self) -> int:
        "get initialize column from user input"
        while True:
            col = int(input(""))
            if col >= 4 and col <=16 and col%2 == 0:
                return col
            else:
                print("invalid column input")

    def get_choice(self) -> int:
        "choice used to get game mode"
        while True:
            choice = input("")
            if choice == '>' or choice == '<':
                return choice

    def get_first_turn(self)-> str:
        "user input to get first turn"
        while True:
            player = input("")
            if player == 'B':
                return 'B'
            if player == 'W':
                return 'W'
            else:
                print("invalid player")

    def get_row_col(self) -> int:
        "input to get row from user"
        while True:
            try:
                string = input().split(" ")
                row = int(string[0])
                col = int(string[1])
                return (row, col)
            except:
                print("Try Again")
                continue
           

class Game:
    def __init__(self, board: board.Board, choice:Input.get_choice,
                 first_turn: Input.get_first_turn) -> None:
        self._board = board
        self._current_kind = first_turn
        self._choice = choice

    def initialize(self):
        "sets up game pre setting before game starts"
        row1 = self._board.get_rows()//2 -1
        col1 = self._board.get_columns()//2-1
        row = self._board.get_rows()//2
        col = self._board.get_columns()//2
        self.set_piece(row1, col1)
        self.switch_turns()
        self.set_piece(row1 , col)
        self.switch_turns()
        self.set_piece(row, col)
        self.switch_turns()
        self.set_piece(row, col1)
        self.switch_turns()

    def run(self):
        "start game"        
        while True:
            print("COUNT")
            print("B: {} W: {}\n".format(self._board.black_count(),
                                              self._board.white_count()))
            ally_moves = self.ally_can_move()
            #print("ally_moves:", ally_moves)
            enemy_moves = self.enemy_can_move()
            #print("enemy_moves:", enemy_moves)
            if ally_moves == False and enemy_moves == False:
                if self._choice == '>':
                    self.most_win()
                elif self._choice == '<':
                    self.less_win()
                break
            
            #to make a move
            print("Turn:", self.get_current_player())
            coordinate = Input().get_row_col()
            print()
            success = self.move(coordinate[0]-1, coordinate[1]-1)
            #check for enemy move
            enemy_moves = self.enemy_can_move()
            if enemy_moves == False:
                self.draw()
                print("VALID")
                continue                                
            if success == True:
                print("VALID")
                self.switch_turns()
            print()
            self.draw()

    def ally_can_move(self) -> bool:
        "returns bool to check for ally moves"
        ally_moves = rules.Rules().moveIsAvailable(self._board, self.get_ally_kind(),self.get_enemy_kind())
        return ally_moves

    def enemy_can_move(self) -> bool:
        "returns bool to check for enemy moves"
        enemy_moves = rules.Rules().moveIsAvailable(self._board, self.get_enemy_kind(), self.get_ally_kind())
        return enemy_moves
            
    def get_board(self) -> board.Board:
        "returns the board object stored in game"
        return self._board

    def most_win(self):
        "winning game mode function for most piece win mode"
        black_list =[]
        white_list = []
        for rows in self._board.get_board():
            for piece in rows:
                if piece.get_kind() == 'B':
                    black_list.append(piece)
                if piece.get_kind() == 'W':
                    white_list.append(piece)
        if len(white_list) > len(black_list):
            return "WINNER: WHITE"
        if len(white_list) == len(black_list):
            return "WINNER: TIE"
        elif len(black_list) > len(white_list):
            return "WINNER: BLACK"
        
            
    def less_win(self):
        "winning game mode function for least piece win mode"
        black_list =[]
        white_list = []
        for rows in self._board.get_board():
            for piece in rows:
                if piece.get_kind() == 'B':
                    black_list.append(piece)
                if piece.get_kind() == 'W':
                    white_list.append(piece)
        if len(white_list) < len(black_list):
            return "WINNER: WHITE"
        if len(white_list) == len(black_list):
            return "WINNER: TIE"
        elif len(black_list) > len(white_list):
            return "WINNER: BLACK"
    
    #choice is an input to decide game mode
    
    def get_current_player(self) -> str:
        "gets the current player in the game"
        return self._current_kind
    
    def get_ally_kind(self) -> str:
        "gets other ally kind in the game"
        return self._current_kind

    def get_choice(self) -> str:
        "gets the game mode choice from user"
        return self._choice
    
    def get_enemy_kind(self) -> str:
        "gets the enemy kind of the current player"
        if self._current_kind == "B":
            return "W"
        if self._current_kind == "W":
            return "B"

    def set_piece(self, row: int, col: int) -> None:
        "makes a move on the board"
        self._board.set_piece(row, col, self.get_ally_kind())
        

    def print_piece_list(self, pieces:list) -> None:
        "used to print piece attributes to string"
        for piece in pieces:
            print(piece.to_string())
        
    def move(self, row: int, col: int) -> bool:
        "makes the move after checking if move is valid"
        # displaying move
        # move must be on grid
        if not rules.Rules().moveIsOnGrid(self._board, row, col):
            #print("INVALID: move is off grid")
            return False
        # move must be available
        if rules.Rules().moveIsTaken(self._board, row, col):
            #print("INVALID: move is unavailable")
            return False
        # move must have adjacent enemies
        if not rules.Rules().moveHasAdjacentEnemies(self._board, row, col, self.get_enemy_kind()):
            #print("INVALID: no adjacent opponents")
            return False;
        # move must have flippable enemies
        if not rules.Rules().moveHasFlippableEnemies(self._board, row, col, self.get_ally_kind(), self.get_enemy_kind()):
            #print("INVALID: no flippable opponents")
            return False;
        # all conditions are satisfied
        self._board.set_piece(row, col, self.get_ally_kind());
        # flipping pieces
        pieces = search.Search().getFlippableEnemies(self._board, row, col, self.get_ally_kind(), self.get_enemy_kind());
        for piece in pieces:
            piece.flip()
        return True
                              
    def switch_turns(self):
        "used to switch turns after a move"
        self._current_kind = self.get_enemy_kind()

    def draw(self):
        "draws the game board"
        self._board.draw()
