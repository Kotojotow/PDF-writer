import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox 
from tkinter import filedialog
from tkinter import ttk
import datetime
from datetime import date
import PDF_Writer
import DataBase
import window_class as wc

program_version = "1.01"

def def_statut():
    def statut_save():
        file_read = t.get(1.0,END)
        wc.atrybut.own_statut = file_read[:-1]
        file = open("data/statut.xdd",'w')
        file.write(wc.atrybut.own_statut)
        file.close()
        messagebox.showinfo("Zapisano!","Pomyślnie zapisano regulamin firmy!")
    def statut_view():
        PDF_Writer.create_pdf()
        os.startfile("pdf.pdf")
    statut_screen = Toplevel(MainWindow)
    statut_screen.title('Edycja regulaminu')
    statut_screen.geometry("830x740")
    statut_screen.grab_set()
    t = Text(statut_screen, width=100, height=40,wrap=WORD )
    s = ttk.Scrollbar(statut_screen, orient=VERTICAL, command=t.yview)
    s.grid(column=1, row=0, sticky=(N,S))
    t['yscrollcommand'] = s.set
    t.grid(column=0,row=0)
    t.insert(INSERT, wc.atrybut.own_statut)
    Statut_button = Button(statut_screen, text="Zapisz",padx=50,pady=10,command= statut_save )
    Statut_button.grid(column=0,row=1)
    Statut_button1 = Button(statut_screen, text="Podgląd",padx=50,pady=10,command= statut_view )
    Statut_button1.grid(column=0,row=2)
    

def path_edit():
    dirname = filedialog.askdirectory(title="Wybierz folder docelowy")
    wc.atrybut.own_dir = dirname
    wc.atrybut.owner_save()

def owner_edit():
    def owner_save1():
        wc.atrybut.own_name1  = edit_screen1.win_entry.get()
        wc.atrybut.own_name2  = edit_screen2.win_entry.get()
        wc.atrybut.own_adres  = edit_screen3.win_entry.get()
        wc.atrybut.own_nip    = edit_screen4.win_entry.get()
        wc.atrybut.own_contact= edit_screen5.win_entry.get()
        wc.atrybut.owner_save()
        owner_edit_screen.destroy()

    owner_edit_screen = Toplevel(MainWindow)
    owner_edit_screen.title('Edycja danych firmy')
    owner_edit_screen.geometry("360x180")
    owner_edit_screen.grab_set()
    
    edit_screen1= wc.window_label(owner_edit_screen,"Nazwa: ",0,0)
    edit_screen2= wc.window_label(owner_edit_screen,"Nazwa: ",0,1)
    edit_screen3= wc.window_label(owner_edit_screen,"Adres: ",0,2)
    edit_screen4= wc.window_label(owner_edit_screen,"Nip: ",0,3)
    edit_screen5= wc.window_label(owner_edit_screen,"Kontakt:",0,4)
    edit_screen1.win_entry.insert(0, wc.atrybut.own_name1)
    edit_screen2.win_entry.insert(0, wc.atrybut.own_name2)
    edit_screen3.win_entry.insert(0, wc.atrybut.own_adres)
    edit_screen4.win_entry.insert(0, wc.atrybut.own_nip)
    edit_screen5.win_entry.insert(0, wc.atrybut.own_contact)

    Nip_button = Button(owner_edit_screen, text="Zapisz",padx=50,pady=10,command= owner_save1 )

    Nip_button.grid(column=1,row=6)
    
def check_out():
    wc.dd.zlece1 = wc.five_string(zlec1.win_entry.get(),zlec2.win_entry.get(),zlec3.win_entry.get(),zlec4.win_entry.get(),zlec5.win_entry.get() )
    wc.dd.zlece2 = wc.five_string(zlecb1.win_entry.get(),zlecb2.win_entry.get(),zlecb3.win_entry.get(),zlecb4.win_entry.get(),zlecb5.win_entry.get() )
    wc.dd.msc1 = wc.five_string(zal1.win_entry.get(),zal2.win_entry.get(),zal3.win_entry.get(),zal4.win_entry.get(),zal5.win_entry.get())
    wc.dd.msc2 = wc.five_string(roz1.win_entry.get(),roz2.win_entry.get(),roz3.win_entry.get(),roz4.win_entry.get(),roz5.win_entry.get())
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
    PDF_Writer.create_pdf()
    os.startfile("pdf.pdf")
    pomoc = messagebox.askyesno("Czy chcesz zapisać dokument?","Zapisane dokumenty można otworzyć ponownie później!")
    if pomoc == 1:
        file_name = wc.forbidden_chars(wc.dd.do) + ".pdf"
        file_dir = wc.atrybut.own_dir+"/"+file_name
        is_file = os.path.isfile(file_dir)
        if is_file == 1:
            pomoc1 = messagebox.askokcancel("Dokument już istnieje!","Dokument o takiej nazwie już istnieje, chcesz go nadpisać?")
            if pomoc1 == 1:
                wc.dd.Add_record()
                wc.dd.do_save = 1
                PDF_Writer.create_pdf()
                wc.dd.do_save = 0
                messagebox.showinfo("Zapisano!","Pomyślnie zapisano dokument")
    
###########################################################
MainWindow = Tk()
MainWindow.title('PDF Writer')
MainWindow.geometry("820x570+10+10")
MainWindow.iconbitmap('icons/icon.ico')
                                                                                                                                         
menubar = tk.Menu(MainWindow)
MainWindow.config(menu=menubar)

now = datetime.datetime.now()
wc.dd.Create_data_base()
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='Przegląd Dokumentów',command=DataBase.baza_danych)
filemenu.add_command(label='Ustal folder dla dokumentów',command=path_edit)
filemenu.add_separator()
filemenu.add_command(label='Zmień Dane Firmy',command=owner_edit)
filemenu.add_command(label='Zmień Regulamin',command=def_statut)

menubar.add_cascade(label='Opcje',menu=filemenu)

##############################################################
zlec_label = wc.window_label1(MainWindow,"Zleceniodawca:",1,0)

zlec1 = wc.window_label(MainWindow,"Nazwa:",0,1)
zlec1.win_entry.insert(0, wc.atrybut.own_name1)
zlec2 = wc.window_label(MainWindow,"Nazwa:",0,2)
zlec2.win_entry.insert(0, wc.atrybut.own_name2)
zlec3 = wc.window_label(MainWindow,"Adres:",0,3)
zlec3.win_entry.insert(0, wc.atrybut.own_adres)
zlec4 = wc.window_label(MainWindow,"Nip:",0,4)
zlec4.win_entry.insert(0, wc.atrybut.own_nip)
zlec5 = wc.window_label(MainWindow,"Kontakt:",0,5)
zlec5.win_entry.insert(0, wc.atrybut.own_contact)

zlec_label = wc.window_label1(MainWindow,"Zleceniobiorca:",3,0)

zlecb1 = wc.window_label(MainWindow,"Nazwa:",2,1)
zlecb2 = wc.window_label(MainWindow,"Nazwa:",2,2)
zlecb3 = wc.window_label(MainWindow,"Adres:",2,3)
zlecb4 = wc.window_label(MainWindow,"Nip:",2,4)
zlecb5 = wc.window_label(MainWindow,"Kontakt:",2,5)

zlec_label = wc.window_label1(MainWindow,"Miejsce załadunku:",1,6)

zal1 = wc.window_label(MainWindow,"Nazwa:",0,7)
zal2 = wc.window_label(MainWindow,"Nazwa:",0,8)
zal3 = wc.window_label(MainWindow,"Adres:",0,9)
zal4 = wc.window_label(MainWindow,"Nip:",0,10)
zal5 = wc.window_label(MainWindow,"Kontakt:",0,11)

zlec_label = wc.window_label1(MainWindow,"Miejsce rozładunku:",3,6)

roz1 = wc.window_label(MainWindow,"Nazwa:",2,7)
roz2 = wc.window_label(MainWindow,"Nazwa:",2,8)
roz3 = wc.window_label(MainWindow,"Adres:",2,9)
roz4 = wc.window_label(MainWindow,"Nip:",2,10)
roz5 = wc.window_label(MainWindow,"Kontakt:",2,11)

zlec_label = wc.window_label1(MainWindow,"Dane kierowcy:",1,12)

kie1 = wc.window_label(MainWindow,"Pojazd:",0,13)
kie2 = wc.window_label(MainWindow,"Naczepa:",0,14)
kie3 = wc.window_label(MainWindow,"Dane kierowcy:",0,15)
kie4 = wc.window_label(MainWindow,"Telefon:",0,16)
kie5 = wc.window_label(MainWindow,"Nr. Dowodu:",0,17)

sta = wc.window_label(MainWindow,"Stawka",2,13)
ter = wc.window_label(MainWindow,"Termin Płatności",2,14)
opi = wc.window_label(MainWindow,"Opis Towaru:",2,15)
dok = wc.window_label(MainWindow,"Nr Dokumentu:",2,16)
dok.win_entry.insert(0,str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"/1")
dat = wc.window_label(MainWindow,"Data Zadania:",2,17)
dat.win_entry.insert(0,date.today() )

view_button = Button(MainWindow, text="Podgląd",padx=50,pady=20, command= check_out )
view_button.grid(column=3,row=23)

MainWindow.mainloop()