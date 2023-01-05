from tkinter import Label
from tkinter import Button
from tkinter import messagebox
from tkinter import Toplevel
from tkinter import ttk
from tkinter import *
from tkinter import filedialog

from os import startfile

import sqlite3

from PDF_Writer import create_pdf
from help_class import Label as hc

class parametry:
    def __init__(self, il, st, li):
        self.ilosc = il
        self.strona = st
        self.licznik = li

class data_base_sheet:
    def __init__(self,zlece1,zlece2,msc1,msc2,k1,k2,k3,k4,k5,st,te,op,do,da):
        self.zlece1=zlece1
        self.zlece2=zlece2
        self.msc1=msc1
        self.msc2=msc2
        self.k1=k1
        self.k2=k2
        self.k3=k3
        self.k4=k4
        self.k5=k5
        self.st=st
        self.te=te
        self.op=op
        self.do=do
        self.da=da
    
    do_save = 0
        
    def Create_data_base(self):
        database = sqlite3.connect('data/baza_dokumenty.db')
        c = database.cursor()
        
        c.execute("""create table if not exists klienci(
        zlece1 text,
        zlece2 text,
        msc1 text,
        msc2 text,
        k1 text,
        k2 text,
        k3 text,
        k4 text,
        k5 text,
        st text,
        te text,
        op text,
        do text,
        da text
            )""")
        database.commit()
        database.close()
        
    def Add_record(self):
        database = sqlite3.connect('data/baza_dokumenty.db')
        c = database.cursor()
        c.execute("INSERT INTO klienci VALUES( :zlece1,:zlece2,:msc1,:msc2,:k1,:k2,:k3,:k4,:k5,:st,:te,:op,:do,:da) ",
        {
            'zlece1':self.zlece1,
            'zlece2':self.zlece2,
            'msc1':self.msc1,
            'msc2':self.msc2,
            'k1':self.k1,
            'k2':self.k2,
            'k3':self.k3,
            'k4':self.k4,
            'k5':self.k5,
            'st':self.st,
            'te':self.te,
            'op':self.op,
            'do':self.do,
            'da':self.da
        })
        database.commit()
        database.close()    
        
    def add_document(self):
        self.Add_record()
        self.do_save = 1
        create_pdf(self,atrybut)
        self.do_save = 0
        messagebox.showinfo("Zapisano!","Pomyślnie zapisano dokument")
        
    def baza_danych(self):
        def next_page():
            if pam.ilosc>7*pam.strona:
                pam.strona+=1
                wyswietlanie_strony()
        def prev_page():
            if pam.strona>1:
                pam.strona-=1
                wyswietlanie_strony()
        def podglad(zmienna):
            create_pdf(table[zmienna],atrybut)
            startfile("pdf.pdf")
        def wyswietlanie_strony():
            i = len(table_buttons)
            strona_label = Label(baza_screen,pady=3, text = "")
            for zm in range(i):
                table_buttons[zm].destroy()
                table_labels[zm].destroy()
                table_labels1[zm].destroy()
                table_labels2[zm].destroy()
                table_labels3[zm].destroy()
                table_labels4[zm].destroy()
                strona_label.destroy()
            table_buttons.clear() 
            table_labels.clear()
            table_labels1.clear()
            table_labels2.clear()
            table_labels3.clear()
            table_labels4.clear()
            for zm in range (0,7):
                if pam.ilosc>zm+((pam.strona-1)*7):
                    table_labels.append( Label(baza_screen,text=table[zm+((pam.strona-1)*7)].do))                
                    table_labels[zm].grid(column=0,row=zm+3)
                    table_labels1.append(Label(baza_screen,text=table[zm+((pam.strona-1)*7)].zlece2))
                    table_labels1[zm].grid(column=1,row=zm+3)
                    table_labels2.append(Label(baza_screen,text=table[zm+((pam.strona-1)*7)].st))
                    table_labels2[zm].grid(column=2,row=zm+3)
                    table_labels3.append(Label(baza_screen,text=table[zm+((pam.strona-1)*7)].da))
                    table_labels3[zm].grid(column=3,row=zm+3)
                    table_labels4.append(Label(baza_screen,text=table[zm+((pam.strona-1)*7)].te))
                    table_labels4[zm].grid(column=4,row=zm+3)
                    strona_label = Label(baza_screen,text="Strona:"+str(pam.strona),pady=10)
                    strona_label.grid(column=2, row=0)
                    xz = ((pam.strona-1)*7)+ zm
                    table_buttons.append( Button(baza_screen,text="Podgląd", command=lambda xz=xz: podglad(xz) ) )
                    table_buttons[zm].grid(column=5,row=zm+3)
                else:
                    break
        table = []
        table_buttons = []
        table_labels = []
        table_labels1 = []
        table_labels2 = []
        table_labels3 = []
        table_labels4 = []
        pam = parametry(0,1,0)
        database = sqlite3.connect('data/baza_dokumenty.db')
        c = database.cursor()
        c.execute("SELECT *, oid FROM klienci")
        records = c.fetchall()
        records.reverse()
        for r in records:
            table.append(data_base_sheet(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13]))
            pam.ilosc+=1
        database.commit()
        database.close()

        baza_screen = Toplevel()
        baza_screen.title('Baza Dokumentów')
        baza_screen.geometry("560x670")
        baza_screen.grab_set()

        label1= Label(baza_screen,text="Nr. Dokumentu")
        label2= Label(baza_screen,text="Zleceniobiorca")
        label3= Label(baza_screen,text="Cena Frachtu")
        label4= Label(baza_screen,text="Data Zadania")
        label5= Label(baza_screen,text="Termin Płatności")
        button_next = Button(baza_screen, text= "Nastepna strona",command=next_page)
        button_prev = Button(baza_screen, text= "Poprzednia strona",command=prev_page)

        button_next.grid(column=1, row=0)
        button_prev.grid(column=0, row=0)
        label1.grid(row=2,column=0)
        label2.grid(row=2,column=1)
        label3.grid(row=2,column=2)
        label4.grid(row=2,column=3)
        label5.grid(row=2,column=4)

        wyswietlanie_strony()
        
   
class atrybuty:
    own_name1 =""
    own_name2 =""
    own_adres =""
    own_nip= ""
    own_contact =""
    own_dir = ""
    own_statut = ""
    
    def __init__(self):
        file1 = open("data/owner.xdd","r")
        for a in file1:
            help_s = a[:-1]
            help_list = help_s.split("=")
            match help_list[0]:
                case 'name1':
                    self.own_name1 = help_list[1]
                case 'name2':
                    self.own_name2 = help_list[1]
                case 'adres':
                    self.own_adres = help_list[1]
                case 'nip':
                    self.own_nip = help_list[1]
                case 'contact':
                    self.own_contact = help_list[1]
                case 'dir':
                    self.own_dir = help_list[1]
        file1.close()
        file2 = open("data/statut.xdd","r")
        self.own_statut = file2.read()
        file2.close()
    
    def owner_save(self):
        file = open("data/owner.xdd",'w')
        file.write("name1="+self.own_name1)
        file.write("\n")
        file.write("name2="+self.own_name2)
        file.write("\n")
        file.write("adres="+self.own_adres)
        file.write("\n")
        file.write("nip="+self.own_nip)
        file.write("\n")
        file.write("contact="+self.own_contact)
        file.write("\n")
        file.write("dir="+self.own_dir)
        file.write("\n")
        file.close()
        messagebox.showinfo("Zapisano!","Pomyślnie zapisano dane firmy!")
    def def_statut(self):
        def statut_save():
            file_read = t.get(1.0,END)
            self.own_statut = file_read[:-1]
            file = open("data/statut.xdd",'w')
            file.write(self.own_statut)
            file.close()
            messagebox.showinfo("Zapisano!","Pomyślnie zapisano regulamin firmy!")
        def statut_view():
            create_pdf(dd,self)
            startfile("pdf.pdf")
        statut_screen = Toplevel()
        statut_screen.title('Edycja regulaminu')
        statut_screen.geometry("830x740")
        statut_screen.grab_set()
        t = Text(statut_screen, width=100, height=40,wrap=WORD )
        s = ttk.Scrollbar(statut_screen, orient=VERTICAL, command=t.yview)
        s.grid(column=1, row=0, sticky=(N,S))
        t['yscrollcommand'] = s.set
        t.grid(column=0,row=0)
        t.insert(INSERT, self.own_statut)
        Statut_button = Button(statut_screen, text="Zapisz",padx=50,pady=10,command= statut_save )
        Statut_button.grid(column=0,row=1)
        Statut_button1 = Button(statut_screen, text="Podgląd",padx=50,pady=10,command= statut_view )
        Statut_button1.grid(column=0,row=2)
        
    def path_edit(self):
        dirname = filedialog.askdirectory(title="Wybierz folder docelowy")
        self.own_dir = dirname
        self.owner_save()
        
    def owner_edit(self):
        def owner_save1():
            self.own_name1  = edit_screen1.win_entry.get()
            self.own_name2  = edit_screen2.win_entry.get()
            self.own_adres  = edit_screen3.win_entry.get()
            self.own_nip    = edit_screen4.win_entry.get()
            self.own_contact= edit_screen5.win_entry.get()
            self.owner_save()
            owner_edit_screen.destroy()

        owner_edit_screen = Toplevel()
        owner_edit_screen.title('Edycja danych firmy')
        owner_edit_screen.geometry("360x180")
        owner_edit_screen.grab_set()
        
        edit_screen1= hc.window_label(owner_edit_screen,"Nazwa: ",0,0)
        edit_screen2= hc.window_label(owner_edit_screen,"Nazwa: ",0,1)
        edit_screen3= hc.window_label(owner_edit_screen,"Adres: ",0,2)
        edit_screen4= hc.window_label(owner_edit_screen,"Nip: ",0,3)
        edit_screen5= hc.window_label(owner_edit_screen,"Kontakt:",0,4)
        edit_screen1.win_entry.insert(0, self.own_name1)
        edit_screen2.win_entry.insert(0, self.own_name2)
        edit_screen3.win_entry.insert(0, self.own_adres)
        edit_screen4.win_entry.insert(0, self.own_nip)
        edit_screen5.win_entry.insert(0, self.own_contact)

        Nip_button = Button(owner_edit_screen, text="Zapisz",padx=50,pady=10,command= owner_save1 )

        Nip_button.grid(column=1,row=6)
    
        
dd = data_base_sheet("","","","","","","","","","","","","","")
atrybut = atrybuty()