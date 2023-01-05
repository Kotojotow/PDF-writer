from ast import Break, Lambda
from asyncio.windows_events import NULL
import tkinter as tk
from tkinter import *
import sqlite3
import PDF_Writer
import os
import window_class as wc

class parametry:
    def __init__(self, il, st, li):
        self.ilosc = il
        self.strona = st
        self.licznik = li


def baza_danych():
    table = []
    table_buttons = []
    table_labels = []
    table_labels1 = []
    table_labels2 = []
    table_labels3 = []
    table_labels4 = []
    pam = parametry(0,1,0)
    def next_page():
        if pam.ilosc>7*pam.strona:
            pam.strona+=1
            wyswietlanie_strony()
    def prev_page():
        if pam.strona>1:
            pam.strona-=1
            wyswietlanie_strony()

    database = sqlite3.connect('data/baza_dokumenty.db')
    c = database.cursor()
    c.execute("SELECT *, oid FROM klienci")
    records = c.fetchall()
    records.reverse()
    for r in records:
        table.append(wc.data_base_sheet(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13]))
        pam.ilosc+=1
    database.commit()
    database.close()

    #def czyszczenie():
    def podglad(zmienna):
        wc.dd = table[zmienna]
        PDF_Writer.create_pdf()
        os.startfile("pdf.pdf")
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