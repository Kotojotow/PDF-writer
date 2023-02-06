from tkinter import Label
from tkinter import Entry
from tkinter import Toplevel

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
        self.win_label = Label(w_hand,pady=3, text = l_name)
        self.win_entry = Entry(w_hand, width=width)
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