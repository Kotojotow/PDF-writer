from tkinter import Button

import C_help_class as hc
import C_Attributes as wc
import F_data_base

def edit_document(doc_statemant = wc.attributes):
    def character_limit(entry_text, max):
        while hc.width_string(entry_text.get()) > max:
            entry_text.set(entry_text.get()[:-1])
    def check_out():
        doc_statemant.zlece1 = hc.five_string(zlec1.win_entry.get(),zlec2.win_entry.get(),zlec3.win_entry.get(),zlec4.win_entry.get(),zlec5.win_entry.get() )
        doc_statemant.zlece2 = hc.five_string(zlecb1.win_entry.get(),zlecb2.win_entry.get(),zlecb3.win_entry.get(),zlecb4.win_entry.get(),zlecb5.win_entry.get() )
        doc_statemant.msc1   = hc.five_string(zal1.win_entry.get(),zal2.win_entry.get(),zal3.win_entry.get(),zal4.win_entry.get(),zal5.win_entry.get())
        doc_statemant.msc2   = hc.five_string(roz1.win_entry.get(),roz2.win_entry.get(),roz3.win_entry.get(),roz4.win_entry.get(),roz5.win_entry.get())
        doc_statemant.k1     = str(kie1.win_entry.get())
        doc_statemant.k2     = str(kie2.win_entry.get())
        doc_statemant.k3     = str(kie3.win_entry.get())
        doc_statemant.k4     = str(kie4.win_entry.get())
        doc_statemant.k5     = str(kie5.win_entry.get())
        doc_statemant.st     = str(sta.win_entry.get())
        doc_statemant.te     = str(ter.win_entry.get())
        doc_statemant.op     = str(opi.win_entry.get())
        doc_statemant.da     = str(dat.win_entry.get())
        
        doc_statemant.add_document(add=1)
        doc_statemant.edit_record()
        
        F_data_base.data_base()
        edit_doc_screen.destroy()
    
    tab1 = hc.one_string(doc_statemant.zlece1)
    tab2 = hc.one_string(doc_statemant.zlece2)
    tab3 = hc.one_string(doc_statemant.msc1)
    tab4 = hc.one_string(doc_statemant.msc2)
    
    edit_doc_screen = hc.ME_new_window('Edytuj Dokument',"820x570+20+20")
    edit_doc_screen.screen_handle.resizable(0,0)

    zlec_label = hc.window_label1(edit_doc_screen.screen_handle,"Zleceniodawca:",1,0)

    zlec1 = hc.window_label(edit_doc_screen.screen_handle,"Nazwa:",0,1,entry=  tab1[0])
    zlec2 = hc.window_label(edit_doc_screen.screen_handle,"Nazwa:",0,2,entry=  tab1[1])
    zlec3 = hc.window_label(edit_doc_screen.screen_handle,"Adres:",0,3,entry=  tab1[2])
    zlec4 = hc.window_label(edit_doc_screen.screen_handle,"Nip:",0,4,entry=    tab1[3])
    zlec5 = hc.window_label(edit_doc_screen.screen_handle,"Kontakt:",0,5,entry=tab1[4])

    zlec_label = hc.window_label1(edit_doc_screen.screen_handle,"Zleceniobiorca:",3,0)

    zlecb1 = hc.window_label(edit_doc_screen.screen_handle,"Nazwa:",2,1   ,entry=tab2[0])
    zlecb2 = hc.window_label(edit_doc_screen.screen_handle,"Nazwa:",2,2   ,entry=tab2[1])
    zlecb3 = hc.window_label(edit_doc_screen.screen_handle,"Adres:",2,3   ,entry=tab2[2])
    zlecb4 = hc.window_label(edit_doc_screen.screen_handle,"Nip:",2,4     ,entry=tab2[3])
    zlecb5 = hc.window_label(edit_doc_screen.screen_handle,"Kontakt:",2,5 ,entry=tab2[4])
    
    zlec_label = hc.window_label1(edit_doc_screen.screen_handle,"Miejsce za??adunku:",1,6)

    zal1 = hc.window_label(edit_doc_screen.screen_handle,"Nazwa:",0,7    ,entry=tab3[0])
    zal2 = hc.window_label(edit_doc_screen.screen_handle,"Nazwa:",0,8    ,entry=tab3[1])
    zal3 = hc.window_label(edit_doc_screen.screen_handle,"Adres:",0,9    ,entry=tab3[2])
    zal4 = hc.window_label(edit_doc_screen.screen_handle,"Nip:",0,10     ,entry=tab3[3])
    zal5 = hc.window_label(edit_doc_screen.screen_handle,"Kontakt:",0,11 ,entry=tab3[4])

    zlec_label = hc.window_label1(edit_doc_screen.screen_handle,"Miejsce roz??adunku:",3,6)

    roz1 = hc.window_label(edit_doc_screen.screen_handle,"Nazwa:",2,7    ,entry=tab4[0])
    roz2 = hc.window_label(edit_doc_screen.screen_handle,"Nazwa:",2,8    ,entry=tab4[1])
    roz3 = hc.window_label(edit_doc_screen.screen_handle,"Adres:",2,9    ,entry=tab4[2])
    roz4 = hc.window_label(edit_doc_screen.screen_handle,"Nip:",2,10     ,entry=tab4[3])
    roz5 = hc.window_label(edit_doc_screen.screen_handle,"Kontakt:",2,11 ,entry=tab4[4])

    zlec_label = hc.window_label1(edit_doc_screen.screen_handle,"Dane kierowcy:",1,12)

    kie1 = hc.window_label(edit_doc_screen.screen_handle,"Pojazd:",0,13        ,entry=doc_statemant.k1)
    kie2 = hc.window_label(edit_doc_screen.screen_handle,"Naczepa:",0,14       ,entry=doc_statemant.k2)
    kie3 = hc.window_label(edit_doc_screen.screen_handle,"Dane kierowcy:",0,15 ,entry=doc_statemant.k3)
    kie4 = hc.window_label(edit_doc_screen.screen_handle,"Telefon:",0,16       ,entry=doc_statemant.k4)
    kie5 = hc.window_label(edit_doc_screen.screen_handle,"Nr. Dowodu:",0,17    ,entry=doc_statemant.k5)

    sta = hc.window_label(edit_doc_screen.screen_handle,"Stawka",2,13          ,entry=doc_statemant.st)
    ter = hc.window_label(edit_doc_screen.screen_handle,"Termin P??atno??ci",2,14,entry=doc_statemant.te)
    opi = hc.window_label(edit_doc_screen.screen_handle,"Opis Towaru:",2,15    ,entry=doc_statemant.op)
    dat = hc.window_label(edit_doc_screen.screen_handle,"Data Zadania:",2,17,   entry=doc_statemant.da)

    view_button = Button(edit_doc_screen.screen_handle, text="Zapisz",padx=350,pady=16, command= check_out )
    view_button.grid(column=0,row=23,columnspan=4,pady=15)
    
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
    dat.entry_text.trace("w", lambda *args: character_limit(dat.entry_text,110))