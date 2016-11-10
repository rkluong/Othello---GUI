
#Main.py

####################
#to run the program#
####################
#download all the uploaded files into the same directory then execute main.py
#files to download
#board.py
#canvas.py
#widget.py
#game.py
#rules.py
#search.py
#point.py
#piece.py

import board
import canvas
import widget
import game


if __name__ == "__main__":

    settings = widget.Widget()
    settings.main_loop()
    #if cancel_button pressed then don't start game
    if not settings.cancel_button_pressed() == True:
        #configure game setting
        choice = settings.get_game()
        turn = settings.get_turn()
        row = int(settings.get_row())
        column = int(settings.get_column())
        game_mode = settings.get_game()
        first_turn = settings.get_turn()
        board = board.Board(row,column)
        board.game_settings()
        #start game       
        game = game.Game(board,game_mode, first_turn)
        game.initialize()
        canvas = canvas.Canvas(game, row, column)
        

 
    
    
