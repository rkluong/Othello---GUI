#ID#43351454
import piece

class Board:
    def __init__(self, row:int, column:int):
        "attributes for board objects"
        self._list = []
        self._row = row
        self._column = column
        self._white = 0
        self._black = 0
        
    def get_rows(self):
        "returns the row count used to construct the board"
        return self._row

    def get_columns(self):
        "returns the column  cound used to construct the board"
        return self._column

    def get_board(self):
        "returns the list stored inside board class"
        return self._list


    def game_settings(self):
        "constructs a 2d list and appends piece objects inside each list"
        for i in range(self._row):
            self._list.append([])
            for j in range(self._column):
                pieces = piece.Piece(i,j)
                self._list[i].append(pieces)
                

    def set_piece(self, row: int, col: int, kind: str) -> None:
        "updates each piece with a different value in their kind attribute"
        piece = self.get_piece(row, col)
        piece.update(kind);

    def draw(self):
        "displays the game board"
        for _list in self._list:
            for piece in _list:
                if piece.get_kind() == 'B':
                    print('B', end = ' ')
                elif piece.get_kind() == 'W':
                    print('W', end = ' ')
                elif piece.get_kind() == '.':
                    print('.', end = ' ')
            print('\n')
            
    def black_count(self):
        "returns the number of black discs on the board"
        self._black = 0
        for _list in self._list:
            for piece in _list:
                if piece.get_kind() == 'B':
                    self._black += 1
        return self._black

    def white_count(self):
        "returns the number of white discs on the board"
        self._white = 0
        for _list in self._list:
            for piece in _list:
                if piece.get_kind() == 'W':
                	self._white += 1
        return self._white

    def get_piece(self, row:int, column:int):
        "gets the piece at the given row and column"
        while True:
            if row < 0 or column < 0:
                continue
    	#row and column are 1 based
            if row > self._row - 1  or column > self._column- 1:
                continue
            return self._list[row][column]


