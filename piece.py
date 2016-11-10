
class Piece:
    def __init__(self, row:int, col:int):
        "constructs piece class object with set attributes"
        self._row = row
        self._col = col
        self._kind = '.'
        
    def update(self, kind:str):
        "used to update the piece._kind with a given string"
        self._kind = kind
    	
    def get_row(self):
        "return the row coordinate of a given piece object"
        return self._row

    def get_col(self):
        "gets the column coordinate of a given piece"
        return self._col

    def get_kind(self):
        "gets the kind of piece"
        return self._kind

    def flip(self):
        "used to flip pieces on the game board"
        if self._kind == 'B':
            self._kind ='W'
        elif self._kind == 'W':
            self._kind = 'B'

    def to_string(self):
        "returns the coordinate of a given piece object"
        return str("[{},{}] {}".format(self._row, self._col, self._kind))

    def get_fill(self):
        if self._kind == 'B':
            return 'Black'
        elif self._kind == 'W':
            return 'White'

    
        
