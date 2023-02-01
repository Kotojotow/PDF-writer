from tkinter import Button
from tkinter import filedialog
from tkinter import LabelFrame

import C_help_class as hc
import C_Attributes as wc


def path_edit():
    def on_click():
        dirname = filedialog.askdirectory(title="Wybierz folder docelowy")
        print(dirname)
        if dirname != "":
            wc.dd.own_dir = dirname
            wc.dd.owner_save()
            path_edit_window.destroy()
    
    path_edit_window = hc.ME_new_window("Zmiana ścieżki", "500x125+20+20")
    path_edit_window.screen_handle.resizable(1,0)
    frame = LabelFrame(path_edit_window.screen_handle)
    hc.window_label1(frame, "Ścieżka",0,0)
    
    
    if wc.dd.own_dir == "":
        text_dir = "Brak Wybranej ścieżki!"
    else:
        text_dir = wc.dd.own_dir

    hc.window_label1(frame, text_dir,1,0)
    path_button = Button(frame, text="Wybierz katalog docelowy",padx=20,pady=5,command = on_click)
    path_button.grid(column=0,row=1,columnspan=2)
    frame.grid(column=0,row=0,padx=5,pady=5,ipadx=10,ipady=10)
    
    
    