from fpdf import FPDF
import window_class as wc

def create_pdf():
    # create FPDF object
    a_wys=10
    pdf = FPDF('P', 'mm', 'A4')

    # add a page
    pdf.add_page()

    pdf.add_font('dejavu','','fonts/DejaVuSans.ttf',uni = True)
    pdf.set_font('dejavu', '', 12)
    
    # stopka
    
    stopka_wys=30
    pdf.image('img/logo.png',0,0)
    pdf.cell(180, stopka_wys, '',ln = 2)
    pdf.set_xy(130,10)
    pdf.cell(55,7,border = True,txt='Zlecenie Transportowe')
    pdf.set_xy(130,17)
    pdf.cell(55,7,border = True,txt='nr. '+ wc.dd.do)
    pdf.set_xy(130,24)
    pdf.cell(55,7,border = True,txt='z dnia '+ wc.dd.da)
    a_wys+=stopka_wys
    
    # zleceniodawca i biorca
    
    cella_wys=50
    pdf.set_font_size(12)
    pdf.set_xy(10,55)
    pdf.multi_cell(85,6,border = True,txt=wc.dd.zlece1)
    pdf.set_xy(100,55)
    pdf.multi_cell(85,6,border = True,txt=wc.dd.zlece2)
    pdf.set_font_size(15)
    pdf.text(10,a_wys+10,"Zleceniodawca:")
    pdf.text(100,a_wys+10,"Zleceniobiorca:")
    pdf.set_font_size(12)
    a_wys += cella_wys
    
    # Miejsce zaladunku i rozladunku
    
    cellb_wys = 50
    pdf.set_xy(10,105)
    pdf.multi_cell(85,6,border = True,txt=wc.dd.msc1)
    pdf.set_xy(100,105)
    pdf.multi_cell(85,6,border = True,txt=wc.dd.msc2)
    pdf.set_font_size(15)
    pdf.text(10,a_wys+10,"Miejsce Załadunku:")
    pdf.text(100,a_wys+10,"Miejsce Rozładunku:")
    pdf.set_font_size(12)
    a_wys += cellb_wys-5
    
    # Dane Frachtu
    
    cellc_wys = 15
    pdf.cell(180,10,ln = 1)
    pdf.cell(45,cellc_wys,border = True, txt = "Pojazd:", align= 'C')
    pdf.cell(135,cellc_wys,border = True,ln = 1, txt = wc.dd.k1, align= 'C')
    pdf.cell(45,cellc_wys,border = True, txt = "Naczepa:", align= 'C')
    pdf.cell(135,cellc_wys,border = True,ln = 1, txt = wc.dd.k2, align= 'C')
    pdf.cell(45,cellc_wys,border = True, txt = "Dane Kierowcy:", align= 'C')
    pdf.cell(135,cellc_wys,border = True,ln = 1, txt = wc.dd.k3, align= 'C')
    pdf.cell(45,cellc_wys,border = True, txt = "Telefon:", align= 'C')
    pdf.cell(135,cellc_wys,border = True,ln = 1, txt = wc.dd.k4, align= 'C')
    pdf.cell(45,cellc_wys,border = True, txt = "Nr. Dowodu:", align= 'C')
    pdf.cell(135,cellc_wys,border = True,ln = 1, txt = wc.dd.k5, align= 'C')
    pdf.cell(180,10,ln = 1)
    a_wys+=cellc_wys*7-6
    
    #Opis towaru i cena
    
    celld_wys=15
    celle_wys=20
    pdf.cell(45,celld_wys,border = True,txt = "Stawka za Uslugę:", align = "C" )
    pdf.cell(45,celld_wys,border = True,txt = wc.dd.st, align = "C" )
    pdf.cell(45,celld_wys,border = True,txt = "Termin Płatności", align = "C" )
    pdf.cell(45,celld_wys,border = True,ln = 1,txt = wc.dd.te, align = "C" )
    pdf.cell(60,celle_wys,border = True,txt = "Opis Towaru:", align = "C" )
    pdf.cell(120,celle_wys,border = True,ln = 1,txt = wc.dd.op, align = "C" )
    
    #strona1
    
    pdf.set_font_size(9)
    #pdf.text(90,a_wys+50,"Strona 1")
    #pdf.add_page()
    #pdf.image('img/2strona.png',0,0,200)
    pdf.text(90,284,"Strona 2")

    
    pdf.add_page()
    pdf.set_font_size(11)
    pdf.multi_cell(190,6,txt=wc.atrybut.own_statut)
    pdf.cell(190,6,ln = 1 )
    pdf.multi_cell(0,6 ,txt="           Zleceniodawca                                                                               Zleceniobiorca\n   ( data, pieczątka, podpis)                                                              ( data, pieczątka, podpis)\n   ........................................                                                              ........................................")

    if wc.dd.do_save == 1:
        file_name = wc.forbidden_chars(wc.dd.do) + ".pdf"
        file_dir = wc.atrybut.own_dir+"/"+file_name
        pdf.output(file_dir)
    else:
        pdf.output("pdf.pdf")