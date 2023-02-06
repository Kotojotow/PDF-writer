import sqlite3
import requests

from tkinter import messagebox

class Client:
    
    def __init__(self,nip):
        self.nip = nip
        self.client_data = self.find_client(self.nip)
        
    def find_client(self, nip):
        
        database = sqlite3.connect('data/baza_Klienci.db')
        c = database.cursor()
        c.execute("SELECT *, rowid FROM klienci")
        records = c.fetchall()
        database.commit()
        database.close()
        
        for a in records:
            if a[4] == nip:
                return a
        
        zm = self.CEIDG(nip)
        if zm == "<Response [200]>":#OK
            pass
        
        
        
        
        
        if zm == "<Response [204]>":#Nie znaleziono danych w odpowiedzi na podane kryteria wyszukiwania
            self.response204()
            return 0
        if zm == "<Response [401]>":#Brak autoryzacji
            self.response401()
            return 0
        if zm == "<Response [403]>":#Brak uprawnień do zasobu
            self.response403()
            return 0
        if zm == "<Response [404]>":#Zasób nie istnieje
            self.response404()
            return 0
        if zm == "<Response [429]>":#Zbyt wiele zapytań
            self.response429()
            return 0
        if zm == "<Response [500]>":#Wewnętrzny błąd serwera
            self.response500()
            return 0
        
        
    def CEIDG(self,nip):
        headers = {'Authorization' : 'Bearer eyJraWQiOiJjZWlkZyIsImFsZyI6IkhTNTEyIn0.eyJnaXZlbl9uYW1lIjoiTWljaGHFgiIsInBlc2VsIjoiOTcwMzEyMDExNTEiLCJpYXQiOjE2NzI4MDY4ODUsImZhbWlseV9uYW1lIjoiRWpkeXMiLCJjbGllbnRfaWQiOiJVU0VSLTk3MDMxMjAxMTUxLU1JQ0hBxYEtRUpEWVMifQ.H9U-6rU4cUF-bxLvlwj3VfjTIigwssMaenSi62FrilDVAqt-lS3Be-kWZx9Azu1BSbUn5ZhLwhtvnl0OsNZO8A'}
        text = 'https://dane.biznes.gov.pl/api/ceidg/v2/firma?nip=' + nip
        response = requests.get(text, headers=headers)
        return response
   
    def response204(self):
        messagebox.showerror("Błąd wyszukiwania!","Nie znaleziono danych w odpowiedzi na podane kryteria wyszukiwania.")
    def response401(self):
        messagebox.showerror("Błąd wyszukiwania!","Brak autoryzacji, skontaktuj się z administratorem systemu.")
    def response403(self):
        messagebox.showerror("Błąd wyszukiwania!","Brak uprawnień do zasobu, skontaktuj się z administratorem oprogramowania.")
    def response404(self):
        messagebox.showerror("Błąd wyszukiwania!","Zasób nie istnieje.")
    def response429(self):
        messagebox.showerror("Błąd wyszukiwania!","Zbyt wiele zapytań, spróbuj ponownie później, jeżeli błąd powtarza się skontaktuj się z administratorem oprogramowania.")
    def response500(self):
        messagebox.showerror("Błąd wyszukiwania!","Wewnętrzny błąd serwera, spróbuj ponownie później")