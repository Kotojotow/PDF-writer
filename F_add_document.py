from datetime import date
from tkinter import Button
from tkinter import messagebox 

import C_help_class as hc
import C_Attributes as wc
import PDF_Writer

from os import startfile
from os import path

from datetime import datetime

def add_document():
    # def check_out():
    #     wc.dd.zlece1 = hc.five_string(zlec1.win_entry.get(),zlec2.win_entry.get(),zlec3.win_entry.get(),zlec4.win_entry.get(),zlec5.win_entry.get() )
    #     wc.dd.zlece2 = hc.five_string(zlecb1.win_entry.get(),zlecb2.win_entry.get(),zlecb3.win_entry.get(),zlecb4.win_entry.get(),zlecb5.win_entry.get() )
    #     wc.dd.msc1 = hc.five_string(zal1.win_entry.get(),zal2.win_entry.get(),zal3.win_entry.get(),zal4.win_entry.get(),zal5.win_entry.get())
    #     wc.dd.msc2 = hc.five_string(roz1.win_entry.get(),roz2.win_entry.get(),roz3.win_entry.get(),roz4.win_entry.get(),roz5.win_entry.get())
    #     wc.dd.k1 = str(kie1.win_entry.get())
    #     wc.dd.k2 = str(kie2.win_entry.get())
    #     wc.dd.k3 = str(kie3.win_entry.get())
    #     wc.dd.k4 = str(kie4.win_entry.get())
    #     wc.dd.k5 = str(kie5.win_entry.get())
    #     wc.dd.st = str(sta.win_entry.get())
    #     wc.dd.te = str(ter.win_entry.get())
    #     wc.dd.op = str(opi.win_entry.get())
    #     wc.dd.do = str(dok.win_entry.get())
    #     wc.dd.da = str(dat.win_entry.get())
    #     PDF_Writer.create_pdf(wc.dd)
    #     startfile("pdf.pdf")
    #     pomoc = messagebox.askyesno("Czy chcesz zapisać dokument?","Zapisane dokumenty można otworzyć ponownie później!")
    #     if pomoc == 1:
    #         file_name = PDF_Writer.forbidden_chars(wc.dd.do) + ".pdf"
    #         file_dir = wc.dd.own_dir+"/"+file_name
    #         is_file = path.isfile(file_dir)
    #         if is_file == 1:
    #             pomoc1 = messagebox.askokcancel("Dokument już istnieje!","Dokument o takiej nazwie już istnieje, chcesz go nadpisać?")
    #             if pomoc1 == 1:
    #                 wc.dd.add_document()
    #         else:
    #             wc.dd.add_document()
        
    now = datetime.now()
    add_doc_screen = hc.ME_new_window('Dodaj Dokument',"820x570+20+20")
    add_doc_screen.screen_handle.resizable(0,0)
    def show_labels():
        zlec_label = hc.window_label1(add_doc_screen.screen_handle,"Zleceniodawca:",1,0)

        zlec1 = hc.window_label(add_doc_screen.screen_handle,"Nazwa:",0,1,entry=wc.dd.own_name1)
        zlec2 = hc.window_label(add_doc_screen.screen_handle,"Nazwa:",0,2,entry=wc.dd.own_name2)
        zlec3 = hc.window_label(add_doc_screen.screen_handle,"Adres:",0,3,entry=wc.dd.own_adres)
        zlec4 = hc.window_label(add_doc_screen.screen_handle,"Nip:",0,4,entry=wc.dd.own_nip)
        zlec5 = hc.window_label(add_doc_screen.screen_handle,"Kontakt:",0,5,entry=wc.dd.own_contact)

        zlec_label = hc.window_label1(add_doc_screen.screen_handle,"Zleceniobiorca:",3,0)

        zlecb1 = hc.window_label(add_doc_screen.screen_handle,"Nazwa:",2,1)
        zlecb2 = hc.window_label(add_doc_screen.screen_handle,"Nazwa:",2,2)
        zlecb3 = hc.window_label(add_doc_screen.screen_handle,"Adres:",2,3)
        zlecb4 = hc.window_label(add_doc_screen.screen_handle,"Nip:",2,4)
        zlecb5 = hc.window_label(add_doc_screen.screen_handle,"Kontakt:",2,5)

        zlec_label = hc.window_label1(add_doc_screen.screen_handle,"Miejsce załadunku:",1,6)

        zal1 = hc.window_label(add_doc_screen.screen_handle,"Nazwa:",0,7)
        zal2 = hc.window_label(add_doc_screen.screen_handle,"Nazwa:",0,8)
        zal3 = hc.window_label(add_doc_screen.screen_handle,"Adres:",0,9)
        zal4 = hc.window_label(add_doc_screen.screen_handle,"Nip:",0,10)
        zal5 = hc.window_label(add_doc_screen.screen_handle,"Kontakt:",0,11)

        zlec_label = hc.window_label1(add_doc_screen.screen_handle,"Miejsce rozładunku:",3,6)

        roz1 = hc.window_label(add_doc_screen.screen_handle,"Nazwa:",2,7)
        roz2 = hc.window_label(add_doc_screen.screen_handle,"Nazwa:",2,8)
        roz3 = hc.window_label(add_doc_screen.screen_handle,"Adres:",2,9)
        roz4 = hc.window_label(add_doc_screen.screen_handle,"Nip:",2,10)
        roz5 = hc.window_label(add_doc_screen.screen_handle,"Kontakt:",2,11)

        zlec_label = hc.window_label1(add_doc_screen.screen_handle,"Dane kierowcy:",1,12)

        kie1 = hc.window_label(add_doc_screen.screen_handle,"Pojazd:",0,13)
        kie2 = hc.window_label(add_doc_screen.screen_handle,"Naczepa:",0,14)
        kie3 = hc.window_label(add_doc_screen.screen_handle,"Dane kierowcy:",0,15)
        kie4 = hc.window_label(add_doc_screen.screen_handle,"Telefon:",0,16)
        kie5 = hc.window_label(add_doc_screen.screen_handle,"Nr. Dowodu:",0,17)

        sta = hc.window_label(add_doc_screen.screen_handle,"Stawka",2,13)
        ter = hc.window_label(add_doc_screen.screen_handle,"Termin Płatności",2,14)
        opi = hc.window_label(add_doc_screen.screen_handle,"Opis Towaru:",2,15)
        dok = hc.window_label(add_doc_screen.screen_handle,"Nr Dokumentu:",2,16,entry=str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"/1")
        dat = hc.window_label(add_doc_screen.screen_handle,"Data Zadania:",2,17,entry=date.today())

    view_button = Button(add_doc_screen.screen_handle, text="Podgląd",padx=350,pady=16, command= show_labels)
    view_button.grid(column=0,row=23,columnspan=4,pady=15)