from tkinter import *
import sqlite3
from tkinter import messagebox

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
        
class window_label:
    def __init__(self,w_hand,l_name,grid_x,grid_y):
        self.w_hand=w_hand
        self.l_name=l_name
        self.grid_x=grid_x
        self.grid_y=grid_y
        self.win_label = Label(w_hand,pady=3, text = l_name)
        self.win_entry = Entry(w_hand, width=50)
        self.win_label.grid(column = grid_x,row=grid_y)
        self.win_entry.grid(column = grid_x+1,row = grid_y)
        
class window_label1:
    def __init__(self,w_hand,l_name,grid_x,grid_y):
        self.w_hand=w_hand
        self.l_name=l_name
        self.grid_x=grid_x
        self.grid_y=grid_y
        self.win_label = Label(w_hand,pady=6, text = l_name)
        self.win_label.grid(column = grid_x,row=grid_y)
        
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
        #file2_read = file2.read()
        self.own_statut = file2.read()
        #self.own_statut = file2_read[-1]
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
          
def five_string(a,b,c,d,e):
    if e == "":
        return a+"\n"+b+"\n"+c+"\n"+d+"\n\n"
    else:
        return a+"\n"+b+"\n"+c+"\n"+d+"\n"+e
    
def forbidden_chars(a):
    a=a.replace('/',"_")
    a=a.replace( '\\' ,"_")
    a=a.replace(":","_")
    a=a.replace("?","_")
    a=a.replace('"',"_")
    a=a.replace("<","_")
    a=a.replace(">","_")
    a=a.replace("|","_")
    a=a.replace("*","_")
    return a

dd = data_base_sheet("","","","","","","","","","","","","","")
atrybut = atrybuty()