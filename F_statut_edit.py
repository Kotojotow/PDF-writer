from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from os import startfile

import PDF_Writer

import C_help_class as hc
from C_Attributes import *

def F_statut_edit():
    def statut_save():
        file_read = t.get(1.0,END)
        dd.own_statut = file_read[:-1]
        file = open("data/statut.xdd",'w')
        file.write(dd.own_statut)
        file.close()
        statut_screen.destroy()
        messagebox.showinfo("Zapisano!","Pomyślnie zapisano regulamin firmy!")   
    def statut_view():
        PDF_Writer.create_pdf(dd)
        startfile("pdf.pdf")
    statut_screen = hc.ME_new_window('Edycja regulaminu',"850x770+20+20")
    statut_screen.screen_handle.resizable(0,0)
    t = Text(statut_screen.screen_handle, width=100, height=40,wrap=WORD )
    s = ttk.Scrollbar(statut_screen.screen_handle, orient=VERTICAL, command=t.yview)
    s.grid(column=1, row=0, sticky=(N,S))
    t['yscrollcommand'] = s.set
    t.grid(column=0,row=0,padx=10,pady=10)
    t.insert(INSERT, dd.own_statut)
    Statut_button = Button(statut_screen.screen_handle, text="Zapisz",padx=50,pady=10,command= statut_save )
    Statut_button.grid(column=0,row=1,pady=2)
    Statut_button1 = Button(statut_screen.screen_handle, text="Podgląd",padx=50,pady=10,command= statut_view )
    Statut_button1.grid(column=0,row=2,pady=2)