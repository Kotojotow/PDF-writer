from os import startfile
from os import path

import tkinter
from tkinter import Button
from tkinter import messagebox 
from tkinter import Tk
from tkinter import Toplevel

from datetime import datetime
from datetime import date

import window_class as wc
import help_class as hc
import PDF_Writer

program_version = "1.01"

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
    PDF_Writer.create_pdf(wc.dd,wc.atrybut)
    startfile("pdf.pdf")
    pomoc = messagebox.askyesno("Czy chcesz zapisać dokument?","Zapisane dokumenty można otworzyć ponownie później!")
    if pomoc == 1:
        file_name = PDF_Writer.forbidden_chars(wc.dd.do) + ".pdf"
        file_dir = wc.atrybut.own_dir+"/"+file_name
        is_file = path.isfile(file_dir)
        if is_file == 1:
            pomoc1 = messagebox.askokcancel("Dokument już istnieje!","Dokument o takiej nazwie już istnieje, chcesz go nadpisać?")
            if pomoc1 == 1:
                wc.dd.add_document()
        else:
            wc.dd.add_document()
    
###########################################################
# Main window and loop
MainWindow = Tk()
MainWindow.title('PDF Writer')
MainWindow.geometry("820x570+10+10")
MainWindow.iconbitmap('icons/icon.ico')
                                                                                                                                         
menubar = tkinter.Menu(MainWindow)
MainWindow.config(menu=menubar)

now = datetime.now()
wc.dd.Create_data_base()
filemenu = tkinter.Menu(menubar,tearoff=0)
filemenu.add_command(label='Przegląd Dokumentów',command=wc.dd.baza_danych)
filemenu.add_command(label='Ustal folder dla dokumentów',command=wc.atrybut.path_edit)
filemenu.add_separator()
filemenu.add_command(label='Zmień Dane Firmy',command=wc.atrybut.owner_edit)
filemenu.add_command(label='Zmień Regulamin',command=wc.atrybut.def_statut)

menubar.add_cascade(label='Opcje',menu=filemenu)

zlec_label = hc.window_label1(MainWindow,"Zleceniodawca:",1,0)

zlec1 = hc.window_label(MainWindow,"Nazwa:",0,1)
zlec1.win_entry.insert(0, wc.atrybut.own_name1)
zlec2 = hc.window_label(MainWindow,"Nazwa:",0,2)
zlec2.win_entry.insert(0, wc.atrybut.own_name2)
zlec3 = hc.window_label(MainWindow,"Adres:",0,3)
zlec3.win_entry.insert(0, wc.atrybut.own_adres)
zlec4 = hc.window_label(MainWindow,"Nip:",0,4)
zlec4.win_entry.insert(0, wc.atrybut.own_nip)
zlec5 = hc.window_label(MainWindow,"Kontakt:",0,5)
zlec5.win_entry.insert(0, wc.atrybut.own_contact)

zlec_label = hc.window_label1(MainWindow,"Zleceniobiorca:",3,0)

zlecb1 = hc.window_label(MainWindow,"Nazwa:",2,1)
zlecb2 = hc.window_label(MainWindow,"Nazwa:",2,2)
zlecb3 = hc.window_label(MainWindow,"Adres:",2,3)
zlecb4 = hc.window_label(MainWindow,"Nip:",2,4)
zlecb5 = hc.window_label(MainWindow,"Kontakt:",2,5)

zlec_label = hc.window_label1(MainWindow,"Miejsce załadunku:",1,6)

zal1 = hc.window_label(MainWindow,"Nazwa:",0,7)
zal2 = hc.window_label(MainWindow,"Nazwa:",0,8)
zal3 = hc.window_label(MainWindow,"Adres:",0,9)
zal4 = hc.window_label(MainWindow,"Nip:",0,10)
zal5 = hc.window_label(MainWindow,"Kontakt:",0,11)

zlec_label = hc.window_label1(MainWindow,"Miejsce rozładunku:",3,6)

roz1 = hc.window_label(MainWindow,"Nazwa:",2,7)
roz2 = hc.window_label(MainWindow,"Nazwa:",2,8)
roz3 = hc.window_label(MainWindow,"Adres:",2,9)
roz4 = hc.window_label(MainWindow,"Nip:",2,10)
roz5 = hc.window_label(MainWindow,"Kontakt:",2,11)

zlec_label = hc.window_label1(MainWindow,"Dane kierowcy:",1,12)

kie1 = hc.window_label(MainWindow,"Pojazd:",0,13)
kie2 = hc.window_label(MainWindow,"Naczepa:",0,14)
kie3 = hc.window_label(MainWindow,"Dane kierowcy:",0,15)
kie4 = hc.window_label(MainWindow,"Telefon:",0,16)
kie5 = hc.window_label(MainWindow,"Nr. Dowodu:",0,17)

sta = hc.window_label(MainWindow,"Stawka",2,13)
ter = hc.window_label(MainWindow,"Termin Płatności",2,14)
opi = hc.window_label(MainWindow,"Opis Towaru:",2,15)
dok = hc.window_label(MainWindow,"Nr Dokumentu:",2,16)
dok.win_entry.insert(0,str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"/1")
dat = hc.window_label(MainWindow,"Data Zadania:",2,17)
dat.win_entry.insert(0,date.today() )

view_button = Button(MainWindow, text="Podgląd",padx=50,pady=20, command= check_out )
view_button.grid(column=3,row=23)

MainWindow.mainloop()