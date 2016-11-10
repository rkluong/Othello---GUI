
#widget.py
from tkinter import *
import tkinter


class Widget:
    def __init__(self):
       self._master = Tk()
       self._row_variable = StringVar(self._master)
       self._column_variable = StringVar(self._master)
       self._turn_variable = StringVar(self._master)
       self._game_mode = StringVar(self._master)

       #Label
       label = Label(self._master, text = "Othello Settings", font=("Helvetica",16))
       label.grid(row = 1, column = 3)

       #Ok and Cancel button
       ok_button = Button(self._master, text = "OK", font = ("Helvetica", 12), command = self.ok)
       ok_button.grid(row = 7, column = 3)
       cancel_button = Button(self._master, text = "Cancel",
                              font = ("Helvetica", 12), command = self.destroy)
       cancel_button.grid(row = 7, column = 4)
       self._cancel = False

       #Row Widget
       self._row_variable.set("Row Setting") 
       self._row_option = OptionMenu(self._master, self._row_variable, 4,6,8,10,12,14,16)
       self._row_option.grid(row = 2, column = 3, padx = 1, pady = 1)

       #Column Widget
       self._column_variable.set("Column Setting")
       self._column_option = OptionMenu(self._master, self._column_variable, 4,6,8,10,12,14,16)
       self._column_option.grid(row = 2, column = 4, padx = 1, pady = 1)
       
       #Game Mode Widget
       self._game_mode.set("Game Mode")
       self._game_option = OptionMenu(self._master, self._game_mode, ">", "<")
       self._game_option.grid(row = 3, column = 3, padx = 1, pady = 1)

       #Turn Widget
       self._turn_variable.set("First Turn")
       self._turn_option = OptionMenu(self._master, self._turn_variable, "B", "W")
       self._turn_option.grid(row = 3, column = 4, padx = 1, pady = 1)
       
    def main_loop(self):
        "starts the main Loop for widget class"
        return self._master.mainloop()

    def ok(self):
        "sets up attributes to get the value from the user input into widget"
        self._row = self._row_variable.get()
        self._column = self._column_variable.get()
        self._game = self._game_mode.get()
        self._turn = self._turn_variable.get()
        self._master.destroy()
        
    def get_row(self):
        "returns row attribute to configure the game"
        return self._row

    def get_column(self):
        "returns column attribute to configure the game"
        return self._column

    def get_game(self):
        "return game mode option"
        return self._game

    def get_turn(self):
        "returns first player turn used for setting"
        return self._turn
    

    def destroy(self):
        "sets cancel button to true and destroys the widget window"
        self._cancel = True
        self._master.destroy()

    def cancel_button_pressed(self)->bool:
        "returns the value if cancel button was pressed"
        return self._cancel




        
        
        
