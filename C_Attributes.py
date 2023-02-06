import sqlite3

from tkinter import messagebox

from PDF_Writer import create_pdf

class attributes:
    own_name1 =""
    own_name2 =""
    own_adres =""
    own_nip= ""
    own_contact =""
    own_dir = ""
    own_statut = ""
    do_save = 0
    
    def load_owner(self):
        try:
            file1 = open("data/owner.xdd","r")
        except FileNotFoundError:
            pass
        else:
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
        try:
            file2 = open("data/statut.xdd","r")
        except FileNotFoundError:
            pass
        else:
            self.own_statut = file2.read()
            file2.close()
        
    def __init__(self,zlece1,zlece2,msc1,msc2,k1,k2,k3,k4,k5,st,te,op,do,da,oid = 0):
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
        self.oid=oid
        self.load_owner()
    
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
        
        database1 = sqlite3.connect('data/baza_Klienci.db')
        c1 = database1.cursor()
        
        c1.execute("""create table if not exists klienci(
        nazwa1 text,
        nazwa2 text,
        nazwa3 text,
        nazwa4 text,
        nazwa5 text

            )""")
        database1.commit()
        database1.close()
        
    def Add_record(self):
        database = sqlite3.connect('data/baza_dokumenty.db')
        c = database.cursor()
        try:
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
        except sqlite3.OperationalError:
            self.Create_data_base()
            messagebox.showerror("Błąd!","Uszkodzony plik z bazą danych! Zaczekaj kilka sekund!")
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
        finally:
            database.commit()
            database.close()
        
    def edit_record(self):
        database = sqlite3.connect('data/baza_dokumenty.db')
        c = database.cursor()
        
        command = """UPDATE klienci SET
            zlece1 =:zlece1,
            zlece2 =:zlece2,
            msc1 =  :msc1,
            msc2 =  :msc2,
            k1 =    :k1,
            k2 =    :k2,
            k3 =    :k3,
            k4 =    :k4,
            k5 =    :k5,
            st =    :st,
            te =    :te,
            op =    :op,
            do =    :do,
            da =    :da
            
            WHERE oid = :oid"""
        
        c.execute(command, 
                  { "zlece1":self.zlece1,
                    "zlece2":self.zlece2,
                    "msc1"  :self.msc1,
                    "msc2"  :self.msc2,
                    "k1"    :self.k1,
                    "k2"    :self.k2,
                    "k3"    :self.k3,
                    "k4"    :self.k4,
                    "k5"    :self.k5,
                    "st"    :self.st,
                    "te"    :self.te,
                    "op"    :self.op,
                    "do"    :self.do,
                    "da"    :self.da,
                    "oid"   :self.oid
            })
        
        database.commit()
        database.close()
        
    def add_document(self,add = 0):
        if add == 0:
            self.Add_record()
        self.do_save = 1
        create_pdf(self)
        self.do_save = 0
        messagebox.showinfo("Zapisano!","Pomyślnie zapisano dokument")
        
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
        
dd = attributes("","","","","","","","","","","","","","")