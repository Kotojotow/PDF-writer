import tkinter

from tkinter import Tk

import F_owner_edit 
import F_statut_edit 
import F_data_base 
import F_Path_edit
import F_add_document
import C_Attributes as wc

program_version = "1.02"

###########################################################
# Main window and loop
MainWindow = Tk()
MainWindow.title('PDF Writer')
MainWindow.geometry("820x570+10+10")
MainWindow.iconbitmap('icons/icon.ico')
                                                              
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

clients = tkinter.Menu(menubar,tearoff=0)
clients.add_command(label='Dodaj Klienta')
clients.add_command(label='Przegląd klientów')

menubar.add_cascade(label='Opcje',menu=options)
menubar.add_cascade(label='Dokumenty',menu=documents)
menubar.add_cascade(label='Klienci',menu=clients)

MainWindow.mainloop()