from datetime import date
from tkinter import Button
from tkinter import messagebox 
from tkinter import LabelFrame

import C_help_class as hc
import C_Attributes as wc
import C_Client as cc
import PDF_Writer

from os import startfile
from os import path

from datetime import datetime

def add_document():
    
    def character_limit(entry_text, max):
        while hc.width_string(entry_text.get()) > max:
            entry_text.set(entry_text.get()[:-1])
    def show_enters():
        nip = nip_input.win_entry.get()
        if nip != "":
            data = cc.Client(nip)
        add_doc_screen.screen_handle.geometry("900x600")
        frame1.grid(column=0,row=0,padx=5,pady=5,ipadx=10,ipady=10)
        frame2.grid(column=1,row=0,padx=5,pady=5,ipadx=10,ipady=10)
        frame3.grid(column=0,row=1,padx=5,pady=5,ipadx=10,ipady=10)
        frame4.grid(column=1,row=1,padx=5,pady=5,ipadx=10,ipady=10)
        frame5.grid(column=0,row=2,padx=5,pady=5,ipadx=10,ipady=10)
        frame6.grid(column=1,row=2,padx=5,pady=5,ipadx=10,ipady=10)
        frame7.destroy()

        view_button.grid(column=0,row=23,columnspan=4,pady=15)
        
    def check_out():
        wc.dd.zlece1 = hc.five_string(zlec1.win_entry.get(),zlec2.win_entry.get(),zlec3.win_entry.get(),zlec4.win_entry.get(),zlec5.win_entry.get() )
        wc.dd.zlece2 = hc.five_string(zlecb1.win_entry.get(),zlecb2.win_entry.get(),zlecb3.win_entry.get(),zlecb4.win_entry.get(),zlecb5.win_entry.get() )
        wc.dd.msc1 = hc.five_string(zal1.win_entry.get(),zal2.win_entry.get(),zal3.win_entry.get(),zal4.win_entry.get(),zal5.win_entry.get())
        wc.dd.msc2 = hc.five_string(roz1.win_entry.get(),roz2.win_entry.get(),roz3.win_entry.get(),roz4.win_entry.get(),roz5.win_entry.get())
        wc.dd.k1 = str(kie1.win_entry.get())
        wc.dd.k2 = str(kie2.win_entry.get())
        wc.dd.k3 = str(kie3.win_entry.get())
        wc.dd.k4 = str(kie4.win_entry.get())
        wc.dd.k5 = str(kie5.win_entry.get())
        wc.dd.st = str(sta.win_entry.get())
        wc.dd.te = str(ter.win_entry.get())
        wc.dd.op = str(opi.win_entry.get())
        wc.dd.do = str(dok.win_entry.get())
        wc.dd.da = str(dat.win_entry.get())
        PDF_Writer.create_pdf(wc.dd)
        startfile("pdf.pdf")
        pomoc = messagebox.askyesno("Czy chcesz zapisać dokument?","Zapisane dokumenty można otworzyć ponownie później!")
        if pomoc == 1:
            file_name = PDF_Writer.forbidden_chars(wc.dd.do) + ".pdf"
            file_dir = wc.dd.own_dir+"/"+file_name
            is_file = path.isfile(file_dir)
            if is_file == 1:
                pomoc1 = messagebox.askokcancel("Dokument już istnieje!","Dokument o takiej nazwie już istnieje, chcesz go nadpisać?")
                if pomoc1 == 1:
                    wc.dd.add_document()
            else:
                wc.dd.add_document()
        
    now = datetime.now()
    add_doc_screen = hc.ME_new_window('Dodaj Dokument',"260x100+20+20")
    add_doc_screen.screen_handle.resizable(0,0)
    
    nip = ""
    
    ####################### Frames ################################################
    frame1 = LabelFrame(add_doc_screen.screen_handle,text="Zleceniodawca")
    frame2 = LabelFrame(add_doc_screen.screen_handle,text="Zleceniobiorca")
    frame3 = LabelFrame(add_doc_screen.screen_handle,text="Miejsce załadunku")
    frame4 = LabelFrame(add_doc_screen.screen_handle,text="Miejsce rozładunku")
    frame5 = LabelFrame(add_doc_screen.screen_handle,text="Dane kierowcy")
    frame6 = LabelFrame(add_doc_screen.screen_handle,text="Pozostałe")
    
    frame7 = LabelFrame(add_doc_screen.screen_handle,text="Wprowadź nip")
    
    ####################### initiate  Variables ######################################################################################
    zlec1  = hc.window_label(frame1,"Nazwa:",0,1,entry=wc.dd.own_name1    )
    zlec2  = hc.window_label(frame1,"Nazwa:",0,2,entry=wc.dd.own_name2    )
    zlec3  = hc.window_label(frame1,"Adres:",0,3,entry=wc.dd.own_adres    )
    zlec4  = hc.window_label(frame1,"Nip:",0,4,entry=wc.dd.own_nip        )
    zlec5  = hc.window_label(frame1,"      Kontakt:      ",0,5,entry=wc.dd.own_contact)
    zlecb1 = hc.window_label(frame2,"Nazwa:",2,1  )
    zlecb2 = hc.window_label(frame2,"Nazwa:",2,2  )
    zlecb3 = hc.window_label(frame2,"Adres:",2,3  )
    zlecb4 = hc.window_label(frame2,"       Kontakt:       ",2,4    )
    zlecb5 = hc.window_label(frame2,"Nip:",2,5)
    zal1   = hc.window_label(frame3,"Nazwa:",0,7   )
    zal2   = hc.window_label(frame3,"Nazwa:",0,8   )
    zal3   = hc.window_label(frame3,"Adres:",0,9   )
    zal4   = hc.window_label(frame3,"Nip:",0,10    )
    zal5   = hc.window_label(frame3,"      Kontakt:      ",0,11)
    roz1   = hc.window_label(frame4,"Nazwa:",2,7   )
    roz2   = hc.window_label(frame4,"Nazwa:",2,8   )
    roz3   = hc.window_label(frame4,"Adres:",2,9   )
    roz4   = hc.window_label(frame4,"Nip:",2,10    )
    roz5   = hc.window_label(frame4,"       Kontakt:       ",2,11)
    kie1   = hc.window_label(frame5,"Pojazd:",0,13       )
    kie2   = hc.window_label(frame5,"Naczepa:",0,14      )
    kie3   = hc.window_label(frame5,"Dane kierowcy:",0,15)
    kie4   = hc.window_label(frame5,"Telefon:",0,16      )
    kie5   = hc.window_label(frame5,"Nr. Dowodu:",0,17   )
    sta    = hc.window_label(frame6,"Stawka",2,13)
    ter    = hc.window_label(frame6,"Termin Płatności",2,14)
    opi    = hc.window_label(frame6,"Opis Towaru:",2,15)
    dok    = hc.window_label(frame6,"Nr Dokumentu:",2,16,entry=str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"/1")
    dat    = hc.window_label(frame6,"Data Zadania:",2,17,entry=date.today())
    view_button = Button(add_doc_screen.screen_handle, text="Podgląd",padx=350,pady=16, command= check_out)
    ##############################################################################################################################
    frame7.grid(column=0,row=0,padx=5,pady=5,ipadx=10,ipady=10)
    nip_input = hc.window_label(frame7,"Wprowadź nip kontrachenta: ",0,0,width=10)
    nip_button = Button(frame7, text="Potwierdź",command=show_enters)
    nip_button.grid(row=1,column=0,columnspan=2)

    
    zlec1.entry_text.trace("w", lambda *args: character_limit(zlec1.entry_text,213))
    zlec2.entry_text.trace("w", lambda *args: character_limit(zlec2.entry_text,213))
    zlec3.entry_text.trace("w", lambda *args: character_limit(zlec3.entry_text,213))
    zlec4.entry_text.trace("w", lambda *args: character_limit(zlec4.entry_text,213))
    zlec5.entry_text.trace("w", lambda *args: character_limit(zlec5.entry_text,213))
    zlecb1.entry_text.trace("w", lambda *args: character_limit(zlecb1.entry_text,213))
    zlecb2.entry_text.trace("w", lambda *args: character_limit(zlecb2.entry_text,213))
    zlecb3.entry_text.trace("w", lambda *args: character_limit(zlecb3.entry_text,213))
    zlecb4.entry_text.trace("w", lambda *args: character_limit(zlecb4.entry_text,213))
    zlecb5.entry_text.trace("w", lambda *args: character_limit(zlecb5.entry_text,213))
    zal1.entry_text.trace("w", lambda *args: character_limit(zal1.entry_text,213))
    zal2.entry_text.trace("w", lambda *args: character_limit(zal2.entry_text,213))
    zal3.entry_text.trace("w", lambda *args: character_limit(zal3.entry_text,213))
    zal4.entry_text.trace("w", lambda *args: character_limit(zal4.entry_text,213))
    zal5.entry_text.trace("w", lambda *args: character_limit(zal5.entry_text,213))
    roz1.entry_text.trace("w", lambda *args: character_limit(roz1.entry_text,213))
    roz2.entry_text.trace("w", lambda *args: character_limit(roz2.entry_text,213))
    roz3.entry_text.trace("w", lambda *args: character_limit(roz3.entry_text,213))
    roz4.entry_text.trace("w", lambda *args: character_limit(roz4.entry_text,213))
    roz5.entry_text.trace("w", lambda *args: character_limit(roz5.entry_text,213))
    kie1.entry_text.trace("w", lambda *args: character_limit(kie1.entry_text,260))
    kie2.entry_text.trace("w", lambda *args: character_limit(kie2.entry_text,260))
    kie3.entry_text.trace("w", lambda *args: character_limit(kie3.entry_text,260))
    kie4.entry_text.trace("w", lambda *args: character_limit(kie4.entry_text,260))
    kie5.entry_text.trace("w", lambda *args: character_limit(kie5.entry_text,260))
    sta.entry_text.trace("w", lambda *args: character_limit(sta.entry_text,100))
    ter.entry_text.trace("w", lambda *args: character_limit(ter.entry_text,100))
    opi.entry_text.trace("w", lambda *args: character_limit(opi.entry_text,213))
    dok.entry_text.trace("w", lambda *args: character_limit(dok.entry_text,110))
    dat.entry_text.trace("w", lambda *args: character_limit(dat.entry_text,110))