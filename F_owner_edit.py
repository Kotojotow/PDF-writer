from tkinter import Button
from tkinter import LabelFrame

from C_Attributes import *
from C_help_class import *

def F_owner_edit():
    def character_limit(entry_text, max):
        while width_string(entry_text.get()) > max:
            entry_text.set(entry_text.get()[:-1])
    def owner_save1():
        dd.own_name1  = edit_screen1.win_entry.get()
        dd.own_name2  = edit_screen2.win_entry.get()
        dd.own_adres  = edit_screen3.win_entry.get()
        dd.own_nip    = edit_screen4.win_entry.get()
        dd.own_contact= edit_screen5.win_entry.get()
        new_window.destroy()
        dd.owner_save()

    new_window = ME_new_window('Edycja danych firmy',"410x240+20+20")
    new_window.screen_handle.resizable(0,0)
    
    frame = LabelFrame(new_window.screen_handle,text="Dane Firmy")
    
    edit_screen1= window_label(frame,"Nazwa: ",0,0)
    edit_screen2= window_label(frame,"Nazwa: ",0,1)
    edit_screen3= window_label(frame,"Adres: ",0,2)
    edit_screen4= window_label(frame,"Nip: ",0,3)
    edit_screen5= window_label(frame,"Kontakt:",0,4)
    edit_screen1.win_entry.insert(0, dd.own_name1)
    edit_screen2.win_entry.insert(0, dd.own_name2)
    edit_screen3.win_entry.insert(0, dd.own_adres)
    edit_screen4.win_entry.insert(0, dd.own_nip)
    edit_screen5.win_entry.insert(0, dd.own_contact)
    Nip_button = Button(frame, text="Zapisz",padx=50,pady=10,command= owner_save1 )
    Nip_button.grid(column=1,row=6)
    frame.grid(column=0,row=0,padx=20,pady=20,ipadx=10,ipady=10)
    
    edit_screen1.entry_text.trace("w", lambda *args: character_limit(edit_screen1.entry_text,213))
    edit_screen2.entry_text.trace("w", lambda *args: character_limit(edit_screen2.entry_text,213))
    edit_screen3.entry_text.trace("w", lambda *args: character_limit(edit_screen3.entry_text,213))
    edit_screen4.entry_text.trace("w", lambda *args: character_limit(edit_screen4.entry_text,213))
    edit_screen5.entry_text.trace("w", lambda *args: character_limit(edit_screen5.entry_text,213))