from tkinter import LabelFrame
from tkinter import Button
from tkinter import ttk
from tkinter import *

import sqlite3

from os import startfile

from tkinter import messagebox 
import PDF_Writer
import C_help_class as hc
import C_Edit_record 
import C_Attributes

def data_base():
    def sort_column(tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(key=lambda t: t[0], reverse=reverse)

        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        tv.heading(col, command=lambda: sort_column(tv, col, not reverse))
    def view_click():
        try:
            x = tree.focus()
            details = tree.item(x, 'values')
            name = "SELECT * from klienci where oid= " + details[5]
        except IndexError:
            messagebox.showerror("Błąd!","Wybierz element z listy.")
        else: 
            
            db = sqlite3.connect('data/baza_dokumenty.db')
            curr = db.cursor()
            curr.execute(name)
            r = curr.fetchone()
            document = C_Attributes.attributes(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13])
            db.commit()
            db.close()
            
            PDF_Writer.create_pdf(document)
            startfile("pdf.pdf")
        
    def edit_click():
        try:
            x = tree.focus()
            details = tree.item(x, 'values')
            name = "SELECT *,rowid from klienci where oid= " + details[5]
        except IndexError:
            messagebox.showerror("Błąd!","Wybierz element z listy.")
        else: 

            db = sqlite3.connect('data/baza_dokumenty.db')
            curr = db.cursor()
            curr.execute(name)
            r = curr.fetchone()
            document = C_Attributes.attributes(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13],oid=r[14])
            db.commit()
            db.close()
            
            C_Edit_record.edit_document(document)
            baza_screen.destroy()
    
    def delete_click():
        try:
            x = tree.focus()
            details = tree.item(x, 'values')
            help_z = messagebox.askyesno("Ostrzeżenie!","Czy na pewno chcesz usunąć dokument nr: " + details[0]+" ?")
        except IndexError:
            messagebox.showerror("Błąd!","Wybierz element z listy.")
        else: 
            
            if help_z == 1:
                db = sqlite3.connect('data/baza_dokumenty.db')
                curr = db.cursor()
                
                help_f = "DELETE FROM klienci WHERE oid = " + details[5]
                curr.execute(help_f)
                db.commit()
                db.close()
                tree.delete(x)
        
    database = sqlite3.connect('data/baza_dokumenty.db')
    table = []
    try:
        c = database.cursor()
        c.execute("SELECT *, rowid FROM klienci")
    except sqlite3.OperationalError:
        C_Attributes.dd.Create_data_base()
        messagebox.showerror("Błąd!","Uszkodzony plik z bazą danych! Zaczekaj kilka sekund!")
    finally:
        records = c.fetchall()
        records.reverse()
        for r in records:
            table.append(C_Attributes.attributes(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13],oid=r[14]))
        database.commit()
        database.close()
        baza_screen = hc.ME_new_window('Baza Dokumentów',"780x400+20+20")
        baza_screen.screen_handle.resizable(0,0)
        
        tree = ttk.Treeview(baza_screen.screen_handle, columns=('nr_dok','zleceniobiorca','cena','data','termin','id'))
        s = ttk.Scrollbar(baza_screen.screen_handle, orient=VERTICAL, command=tree.yview)
        tree['yscrollcommand'] = s.set
        
        s.grid(column=1, row=0, sticky=(N,S))
        tree.grid(column=0,row=0,padx=50,pady=20)
        
        frame1 = LabelFrame(baza_screen.screen_handle,text="Funkcje")
        frame1.grid(column=0,row=1,padx=20,pady=20)
        
        button_delete = Button(frame1, text="Usuń pozycję", padx=20,pady=5,command=delete_click)
        button_delete.grid(row=0,column=0,padx=40,pady=15)
        button_edit = Button(frame1, text="Edytuj pozycję", padx=20,pady=5,command=edit_click)
        button_edit.grid(row=0,column=1,padx=40,pady=15)
        button_view = Button(frame1, text="Pokaż rekord", padx=20,pady=5,command=view_click)
        button_view.grid(row=0,column=2,padx=40,pady=15)
        
        tree.column("#0", width=0,stretch='NO')
        tree.column('nr_dok', width=150, anchor='center')
        tree.column('zleceniobiorca', width=250, anchor='center')
        tree.column('cena', width=80, anchor='center')
        tree.column('data', width=80, anchor='center')
        tree.column('termin', width=80, anchor='center')
        tree.column("id", width=0,stretch='NO')
        
        tree.heading('#0',text='',anchor='w')
        tree.heading('nr_dok', text = 'Numer Dokumentu', command=lambda: sort_column(tree, "nr_dok", False))
        tree.heading('zleceniobiorca', text='zleceniobiorca', command=lambda: sort_column(tree, "zleceniobiorca", False))
        tree.heading('cena', text='cena', command=lambda: sort_column(tree, "cena", False))
        tree.heading('data', text='data', command=lambda: sort_column(tree, "data", False))
        tree.heading('termin', text='termin', command=lambda: sort_column(tree, "termin", False))
        
        
        
        for a in range(len(table)):
            tree.insert('', 'end',iid=a,values=(table[a].do, hc.one_string(table[a].zlece2,first=1) , table[a].st,table[a].da,table[a].te,table[a].oid))