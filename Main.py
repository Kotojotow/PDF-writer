import tkinter

from tkinter import Tk
from tkinter import LabelFrame
from tkinter import Button

import F_owner_edit 
import F_statut_edit 
import F_data_base 
import F_Path_edit
import F_add_document
import C_Attributes as wc

program_version = "1.03"

###########################################################
# Main window and loop
MainWindow = Tk()
MainWindow.title('PDF Writer') 
MainWindow.geometry("650x200+10+10")
MainWindow.iconbitmap('icons/icon.ico')
MainWindow.attributes('-topmost', False)
                                                              
menubar = tkinter.Menu(MainWindow)
MainWindow.config(menu=menubar)


wc.dd.Create_data_base()
options = tkinter.Menu(menubar,tearoff=0)
options.add_command(label='Ustal folder dla dokumentów',command=F_Path_edit.path_edit)
options.add_command(label='Zmień Dane Firmy',command=F_owner_edit.F_owner_edit)
options.add_command(label='Zmień Regulamin',command=F_statut_edit.F_statut_edit)

documents = tkinter.Menu(menubar,tearoff=0)
documents.add_command(label='Dodaj Dokument',command= F_add_document.add_document)
documents.add_command(label='Przegląd Dokumentów',command=F_data_base.data_base)

frame1 = LabelFrame(MainWindow,text="Opcje")
frame2 = LabelFrame(MainWindow,text="Dokumenty")

Button1 = Button(frame1, text='Dodaj Dokument',padx=20,pady=5,command = F_add_document.add_document)
Button2 = Button(frame1, text='Przegląd Dokumentów',padx=20,pady=5,command=F_data_base.data_base)

Button3 = Button(frame2, text='Ustal folder dla dokumentów',padx=20,pady=5,command = F_Path_edit.path_edit)
Button4 = Button(frame2, text='Zmień Dane Firmy',padx=20,pady=5,command =F_owner_edit.F_owner_edit )
Button5 = Button(frame2, text='Zmień Regulamin',padx=20,pady=5,command = F_statut_edit.F_statut_edit)

Button1.grid(column=0, row=0,padx=10,pady=10)
Button2.grid(column=1, row=0,padx=10,pady=10)
Button3.grid(column=0, row=0,padx=10,pady=10)
Button4.grid(column=1, row=0,padx=10,pady=10)
Button5.grid(column=2, row=0,padx=10,pady=10)

frame1.grid(column=0,row=0,padx=50,pady=10)
frame2.grid(column=0,row=1,padx=50)

MainWindow.mainloop()