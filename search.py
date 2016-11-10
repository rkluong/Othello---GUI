
import board
import piece
import rules

#helper type class used in rules module
class Search:
    def getAdjacentPieces(self, board: board.Board, row:int, column:int)->list:
        "list of all adjacent pieces givent a row,column coordinate"
        pieces = []
        for i in range(3):
            row_delta = i - 1
            for j in range(3):
                col_delta = j - 1
                search_row = row + row_delta
                search_col = column + col_delta
                if (rules.Rules().moveIsOnGrid(board, search_row, search_col)):
                    piece = board.get_piece(search_row, search_col)
                    pieces.append(piece)
        return pieces
    
    
    def getAllMoves(self, board: board.Board, enemy_kind, ally_kind) -> list:
        "list of all available moves pieces on ally_kind"
        move = []
        for row in range(board.get_rows()):
            for col in range(board.get_columns()):
                if rules.Rules().moveIsTaken(board, row, col) == True:
                    continue
                if rules.Rules().moveIsOnGrid(board, row, col) == False:
                    continue
                if rules.Rules().moveHasFlippableEnemies(board, row, col, ally_kind, enemy_kind) == False:
                    continue
                move.append(board.get_piece(row, col))
                
        return move

    def getAdjacentEnemies(self, board: board.Board, row:int, col:int, enemy_kind:str) -> list:
        "collects a list of nearby enemy pieces in a list"
        pieces = []
        adjacent_pieces = self.getAdjacentPieces(board, row, col)
        for piece in adjacent_pieces:
            kind = piece.get_kind();
            if kind == enemy_kind:
                pieces.append(piece)
        return pieces

    #Helper function for getFlippableEnemies
    def getEnemiesInLine(self, board: board.Board,
                         first_enemy: piece.Piece, row_delta:int,
                         col_delta:int)->list:
        'runs at least once and updates the current piece at the end of looop'
        "used in getFlippableEnemies"
        pieces = []
        current_piece = first_enemy
        while True:
            if not current_piece.get_kind() == first_enemy.get_kind():
                break
            pieces.append(current_piece)
            search_row = current_piece.get_row() + row_delta
            search_col = current_piece.get_col() + col_delta
            if not rules.Rules().moveIsOnGrid(board, search_row, search_col):
                break
            current_piece = board.get_piece(search_row, search_col);
        return pieces
    
    #Helper function for getFlippableEnemies
    def allyFoundAtLineEnd(self, board: board.Board, enemy_line: list, row_delta: int, col_delta:int, ally_kind: str) -> bool:
        "used in get flippable enemies function"
        last_piece = enemy_line[len(enemy_line) -1]
        search_row = last_piece.get_row() + row_delta
        search_col = last_piece.get_col() + col_delta
        if not rules.Rules().moveIsOnGrid(board, search_row, search_col):
            return False
        piece = board.get_piece(search_row, search_col)
        if not piece.get_kind() == ally_kind:
            return False
        return True

    def getFlippableEnemies(self, board: board.Board, row: int, col: int, ally_kind: str, enemy_kind: str) -> list:
        "gets a flippable enemies list"
        flippable = []
        # for each adjacent enemy adds to a list
        pieces = self.getAdjacentEnemies(board, row, col, enemy_kind)
        for piece in pieces:
            # get enemies in that line
            row_delta = piece.get_row() - row
            col_delta = piece.get_col() - col
            #line list of enemies in a line in each direction
            line = self.getEnemiesInLine(board, piece, row_delta, col_delta)
            # append to master list
            if self.allyFoundAtLineEnd(board, line, row_delta, col_delta, ally_kind):
                for item in line:
                    flippable.append(item)
        return flippable


        
