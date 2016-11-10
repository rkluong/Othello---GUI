#ID#43351454
from tkinter import *
import tkinter
import math
import point
import board
import game
import rules

class Canvas:
    def __init__(self, game: game.Game, rows: int, cols: int) -> None:
        # global settings
        self._board = game._board
        self._game = game
        self._rows = rows;
        self._cols = cols;
        self._width = 600;
        self._height = 600;
        self._cell_height = self._height/rows;
        self._cell_width = self._width/cols;
        
        # make the canvas
        self._window = tkinter.Tk();
        self._canvas = tkinter.Canvas(
        master = self._window,
        width = self._width,
        height = self._height, 
        background = "green");
        self.draw_canvas()
        self.draw_othello_label()
        self.draw_count_label()
        self.draw_turn_label()
            
        # configure canvas
        #self._canvas.pack(fill = "both", expand = "Yes");
        for i in range(3):
            self._window.rowconfigure(i, weight = 1);
            self._window.columnconfigure(i, weight = 1);
        
        
        # bind mouse click event
        self._canvas.bind('<Button-1>', self.click_handler);
        # bind canvas resize event
        self._canvas.bind('<Configure>', self._canvas_resize)
        
    # --------------------------
    # CANVAS RESIZE EVENT HANDLER
    # --------------------------
    def _canvas_resize(self, event: tkinter.Event) -> None:
        "redraws all the canvas and widgets when window is resized"
        self.clear()
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        self._width = canvas_width
        self._height = canvas_height
        self._cell_height = self._height/self._rows
        self._cell_width = self._width/self._cols
        self.draw_canvas()
        self.draw_lines()
        self.draw_pieces()
        self.draw_turn_label()
        self.draw_count_label()

    # -------------------------
    # MOUSE CLICK EVENT HANDLER
    # -------------------------
    def get_rowcol(self, pixel_x, pixel_y) -> (int, int):
        "returns a (row, column) tuple"
        floor_x = math.floor(pixel_x/self._cell_width)
        floor_y = math.floor(pixel_y/self._cell_height)
        #Adjustment when the x coordinate is the max row since range of board
        #goes from 0 -> 7 on index
        floor_tuple = (floor_x , floor_y )
        return floor_tuple
  
    def get_x0y0(self, row: int, col: int) -> (float, float):
        "gets the top left corner x,y coordinate x0y0 of bound box"
        height = self._cell_height
        width = self._cell_width
        x0_pos = math.floor(row* width)
        y0_pos = math.floor(col * height)
        if x0_pos < 0:
            x0_pos = 0
        if y0_pos < 0:
            y0_pos = 0
        return (x0_pos, y0_pos)

    # get the bottom right position to draw oval
    def get_x1y1(self, row: int, col: int) -> (float, float):
        "gets the bottom left corner x,y coordinate x1y1 of bound box"
        width = self._cell_width
        height = self._cell_height
        x1_pos = math.ceil(row * width)
        y1_pos = math.ceil(col * height)
        return (x1_pos, y1_pos)
    
    # draws an oval where mouse is clicked
    
    def click_handler(self, event: tkinter.Event) -> None:
        "handles the click to draw ovals on the board"
        "clears the canvas and redraw all canvas, pieces, and labels"
        # get row and col positions
        rowcol_tuple = self.get_rowcol(event.x, event.y)
        row = rowcol_tuple[1]
        col = rowcol_tuple[0]
        self.draw_turn_label()
        # check move with game logic then make move
        success = self._game.move(row, col)
        ally_move = self._game.ally_can_move()
        enemy_move = self._game.enemy_can_move()
        if ally_move == False and enemy_move == False:
            if self._game.get_choice() == '>':
                most_win = Label(self._window,
                                 text = "{}".format(self._game.most_win()),
                                 font = ("Helvetica", 16))
                most_win.grid(row = 2, column = 1, sticky = tkinter.N)
            elif self._game.get_choice() == '<':
                less_win = Label(self._window,
                                 text = "{}".format(self._game.less_win()),
                                 font = ("Helvetica", 16))
                less_win.grid(row = 2, column = 1,sticky = tkinter.N)
            # switch turns
        if self._game.enemy_can_move() == True and success == True:
           self._game.switch_turns()
        self.draw_all()
           

    # -------------------------
    # DRAWING CANVAS | LABELS | 
    # -------------------------
    
    def clear(self) -> None:
        "clears the canvas"
        self._canvas.delete('all')

    def draw_all(self) -> None:
        "function used to draw everything"
        self.draw_count_label()
        self.draw_turn_label()
        self.clear()  
        self.draw_lines()
        self.draw_pieces()
        self.draw_canvas()
        self.draw_othello_label()

    def draw_pieces(self) -> None:
        "draws all the pieces in the board and the count label"
        for List in self._board.get_board():
            for piece in List:
                if piece.get_kind() != '.':
                    self.draw_piece(piece)
        self.draw_count_label

    def draw_turn_label(self) -> None:
        "draws turn label"
        current_turn = Label(self._window, text = "TURN:{}".format(self._game.get_current_player()),
                             font = ("Helvetica", 16))
        current_turn.grid(row = 3, column = 0, sticky = tkinter.N)

    def draw_canvas(self) -> None:
        "draws canvas"
        self._canvas.grid(row = 1, column = 1, padx = 10, pady = 10, 
                          sticky = tkinter.W + tkinter. E)
                    
    def draw_piece(self, piece):
        "used in draw pieces to draw all pieces on a board"
        # get oval draw positions
        x0y0_pos = self.get_x0y0(piece.get_col(), piece.get_row())
        x1y1_pos = self.get_x1y1(piece.get_col()+1, piece.get_row()+1)
        # draw the oval
        self._canvas.create_oval(
            x0y0_pos[0],    # oval x0
            x0y0_pos[1],    # oval y0
            x1y1_pos[0],    # oval x1
            x1y1_pos[1],    # oval y1
            fill = piece.get_fill())

    def draw_othello_label(self):
        "draw othello label"
        othello = Label(self._window, text = "OTHELLO GAME", font = ("Helvetica", 16))
        othello.grid(row = 0, column = 1)

    def draw_count_label(self):
        "draw count label"
        white_count = Label(self._window,
                            text = "White count: {}".format(self._board.white_count()),
                            font = ("Helvetica", 16))
        white_count.grid(row = 3, column = 1, sticky = tkinter.N)
        black_count = Label(self._window,
                            text = "Black count: {}".format(self._board.black_count()),
                            font = ("Helvetica", 16))
        black_count.grid(row = 3, column = 2, sticky = tkinter.N)
    
    def draw_lines(self):
        "draw the othello lines forming a grid"
        draw_y_pos = 2;
        draw_x_pos = 2;
        
        # horizontal lines
        for i in range(self._rows + 1):
            # create_line(x0, y0, x1, y1, fill color, line width)
            self._canvas.create_line(
                0,                  # x0_pos = 0
                draw_y_pos,         # y0_pos = current y_pos
                self._width,        # x1_pos = canvas width
                draw_y_pos,         # y1_pos = current y_pos
                fill = "black",    # line color
                width = 5)          # line width
            # update next y position
            draw_y_pos += self._cell_height;
            
        # vertical lines
        for i in range(self._cols + 1):
            # create_line(x0, y0, x1, y1, fill color, line width)
            self._canvas.create_line(
                draw_x_pos,         # x0_pos = current x_pos
                0,                  # y0_pos = 0
                draw_x_pos,         # x1_pos = current x_pos
                self._height,       # y1_pos = canvas height
                fill = "black",    # line color
                width = 5)          # line width
            # update next x position
            draw_x_pos += self._cell_width;



