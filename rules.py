
import board
import search
#helper class to use in the search class
class Rules:

    def moveIsOnGrid(self, board: board.Board, row:int ,column:int)-> bool:
        "checks if the row and the column is on the board"
        if row < 0 or column < 0:
            return False
        if row >= board.get_rows():
            return False
        if column >= board.get_columns():
     	    return False
        return True

    def moveIsTaken(self, board: board.Board, row: int, column: int)-> bool:
        "checks if move is empty on the board"
        piece = board.get_piece(row, column)
        if piece.get_kind() == '.':
            return False
        else:
            return True

    def moveHasAdjacentEnemies(self, board:board.Board ,row: int, column: int, enemy_kind: str)-> bool:
        "takes in the enemy str to check if there are adjacent enemies at row & col of the board"
        pieces = search.Search().getAdjacentEnemies(board, row, column, enemy_kind)
        if len(pieces) > 0:
            return True
        return False;

    def moveIsAvailable(self, board: board.Board, ally_kind, enemy_kind):
        "checks for all possible moves for a disc color"
        piece = search.Search().getAllMoves(board, enemy_kind, ally_kind)
        if len(piece) > 0:
            return True
        return False

    def moveHasFlippableEnemies(self,board: board.Board, row:int, 
                                column: int, ally_kind:str,
                                enemy_kind:str) -> bool:
        "checks if the move has enemies nearby to flip"
        pieces = search.Search().getFlippableEnemies(board, row,  column, ally_kind, enemy_kind);
        if len(pieces) > 0:
            return True
        return False
    


    
