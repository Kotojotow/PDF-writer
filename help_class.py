from tkinter import Label
from tkinter import Entry

class window_label:
    def __init__(self,w_hand,l_name,grid_x,grid_y):
        self.w_hand=w_hand
        self.l_name=l_name
        self.grid_x=grid_x
        self.grid_y=grid_y
        self.win_label = Label(w_hand,pady=3, text = l_name)
        self.win_entry = Entry(w_hand, width=50)
        self.win_label.grid(column = grid_x,row=grid_y)
        self.win_entry.grid(column = grid_x+1,row = grid_y)
        
class window_label1:
    def __init__(self,w_hand,l_name,grid_x,grid_y):
        self.w_hand=w_hand
        self.l_name=l_name
        self.grid_x=grid_x
        self.grid_y=grid_y
        self.win_label = Label(w_hand,pady=6, text = l_name)
        self.win_label.grid(column = grid_x,row=grid_y)

def five_string(a,b,c,d,e):
    if e == "":
        return a+"\n"+b+"\n"+c+"\n"+d+"\n\n"
    else:
        return a+"\n"+b+"\n"+c+"\n"+d+"\n"+e