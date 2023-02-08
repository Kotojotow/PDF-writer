from tkinter import Label
from tkinter import Entry
from tkinter import Toplevel
from tkinter import *

class ME_new_window() :
    def __init__(self,screen_title,screen_geometry):
        self.screen_handle = Toplevel()
        self.screen_handle.title(screen_title)
        self.screen_handle.geometry(screen_geometry)
        self.screen_handle.grab_set()
    def destroy(self):
        self.screen_handle.destroy()

class window_label:
    def __init__(self,w_hand,l_name,grid_x,grid_y,entry = "",show = 1,width = 50):
        self.__doc__
        self.w_hand=w_hand
        self.l_name=l_name
        self.grid_x=grid_x
        self.grid_y=grid_y
        self.entry_text = StringVar()
        self.win_label = Label(w_hand,pady=3, text = l_name)
        self.win_entry = Entry(w_hand, width=width, textvariable=self.entry_text)
        if entry != "":
            self.win_entry.insert(0, entry)
        self.show_label(show)
    def show_label(self, show):
        if show == 1:
            self.win_label.grid(column = self.grid_x,row=self.grid_y)
            self.win_entry.grid(column = self.grid_x+1,row = self.grid_y)
    def destroy(self):
        self.win_entry.destroy()
        self.win_label.destroy()
        
class window_label1():
    def __init__(self,w_hand,l_name,grid_x,grid_y,cspan = None, rspan = None):
        self.w_hand=w_hand
        self.l_name=l_name
        self.grid_x=grid_x
        self.grid_y=grid_y
        self.win_label = Label(w_hand,pady=6, text = l_name)
        self.win_label.grid(column = grid_x,row=grid_y,columnspan=cspan,rowspan=rspan)

def five_string(a,b,c,d,e):
    if e == "":
        return a+"\n"+b+"\n"+c+"\n"+d+"\n\n"
    else:
        return a+"\n"+b+"\n"+c+"\n"+d+"\n"+e

def one_string(string, first = 0):
    l = string.split("\n")
    if first == 0:
        return l
    else:
        return l[0]
    

def width_string(string):
    total = 0
    for i in string:
        total += width_digit(i)
    return total
        
def width_digit(a):
    match a:
        case 'q' : return 7
        case 'w' : return 9
        case 'e' : return 6
        case 'r' : return 5
        case 't' : return 6
        case 'y' : return 7
        case 'u' : return 7
        case 'i' : return 3
        case 'o' : return 7
        case 'p' : return 7
        case 'a' : return 6
        case 's' : return 5
        case 'd' : return 7
        case 'f' : return 5
        case 'g' : return 7
        case 'h' : return 7
        case 'j' : return 5
        case 'k' : return 6
        case 'l' : return 3
        case 'z' : return 5
        case 'x' : return 5
        case 'c' : return 6
        case 'v' : return 6
        case 'b' : return 7
        case 'n' : return 7
        case 'm' : return 11
        case _: return 7