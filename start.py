#coding:UTF8
import sys
from PyQt4 import QtCore, QtGui
import codecs
from GUI import Ui_MainWindow

def koloruj(klasa): #funkcja przypisująca klasie odpowiedni kolor
    if klasa=='I':
        return(QtGui.QColor('blue'))
    if klasa=='II':
        return(QtGui.QColor('green'))
    if klasa=='III':
        return(QtGui.QColor('yellow'))
    if klasa=='IV':
        return(QtGui.QColor(255,69,0))
    if klasa=='V':
        return(QtGui.QColor('red'))
    else:
        return(QtGui.QColor('black'))

def przekroczenie(x):
    if x==1:
        return(u'normy spełnione')
    if x==0:
        return('<font color="red">normy przekroczone</font>')

def klas_jeziora (biol_el,fiz_el,zan_el):
    #Punkt 1
    if biol_el==1 and fiz_el==1 and zan_el==1:
        return ('I')
    if biol_el==1 and (fiz_el==0 or zan_el==0):
        return ('III')
    if biol_el==2 and fiz_el==1 and zan_el==1:
        return ('II')
    if biol_el==2 and (fiz_el==0 or zan_el==0):
        return ('III')
    if biol_el==3:
        return('III')
    if biol_el==4:
        return('IV')
    if biol_el==5:
        return('V')
    

def klasy(typ,schindler,lista): #funkcja przypisująca wskaźnikom odpowiednie klasy
    listaklas=[]
    licznik=0
    for i in lista:
        if licznik==0:    
            listaklas.append(chlorofil(i,typ,schindler))
        if licznik==1:
            listaklas.append(ioj(i))
        if licznik==2:
            listaklas.append(mise(i,typ))
        if 2<licznik<=8:
            listaklas.append(hydromorf(i))
        if licznik==9:
            listaklas.append(secchi(i,typ, schindler))
        if licznik==10:
            listaklas.append(tlen1(i))
        if licznik==11:
            listaklas.append(tlen2(i))
        if licznik==12:
            listaklas.append(przew(i))
        if licznik==13:
            listaklas.append(azot(i,typ, schindler))
        if licznik==14:
            listaklas.append(fosfor(i,typ, schindler))
        if licznik==15:
            listaklas.append(aldehyd(i))
        if licznik==16:
            listaklas.append(arsen(i))
        if licznik==17:
            listaklas.append(bar(i))
        if licznik==18:
            listaklas.append(bor(i))
        if licznik==19:
            listaklas.append(chrom6(i))
        if licznik==20:
            listaklas.append(chrom(i))
        if licznik==21:
            listaklas.append(cynk(i))
        if licznik==22:
            listaklas.append(miedz(i))
        if licznik==23:
            listaklas.append(I_F(i))
        if licznik==24:
            listaklas.append(IOM(i))
        if licznik==25:
            listaklas.append(glin(i))
        if licznik==26:
            listaklas.append(cyjankiw(i))
        if licznik==27:
            listaklas.append(cyjankiz(i))
        if licznik==28:
            listaklas.append(molibden(i))
        if licznik==29:
            listaklas.append(selen(i))
        if licznik==30:
            listaklas.append(srebro(i))
        if licznik==31:
            listaklas.append(tal(i))
        if licznik==32:
            listaklas.append(tytan(i))
        if licznik==33:
            listaklas.append(wanad(i))
        if licznik==34:
            listaklas.append(antymon(i))
        if licznik==35:
            listaklas.append(fluorki(i))
        if licznik==36:
            listaklas.append(beryl(i))
        if licznik==37:
            listaklas.append(kobalt(i))
        licznik+=1                
    return(listaklas)            

def chlorofil(i,typ,schindler): #funkcja określająca w której wartości granicznej znajduje się chlorofil
    if typ=='1a' or typ=='2a' or typ=='3a' or typ=='5a' or typ=='6a' or typ=='7a':
        if schindler<=2:
            if i[0]<5:
                return (1)
            elif 5<=i[0]<=8:
                return(2)
            elif 8<=i[0]<=11:
                return (3)
            elif 11<=i[0]<=16:
                return(4)
            elif i[0]>16:
                return 5
        if schindler>2:
            if i[0]<7:
                return (1)
            elif 7<=i[0]<=13:
                return(2)
            elif 13<=i[0]<=21:
                return (3)
            elif 21<=i[0]<=33:
                return(4)
            elif i[0]>33:
                return 5
    if typ=='1b' or typ=='2b' or typ=='3b' or typ=='4' or typ=='5b' or typ=='6b' or typ=='7b':
        if schindler<=2:
            if i[0]<10:
                return (1)
            elif 10<=i[0]<=19:
                return(2)
            elif 19<=i[0]<=30:
                return (3)
            elif 30<=i[0]<=42:
                return(4)
            elif i[0]>42:
                return 5
        if schindler>2:
            if i[0]<10:
                return (1)
            elif 10<=i[0]<=23:
                return(2)
            elif 23<=i[0]<=40:
                return (3)
            elif 40<=i[0]<=68:
                return(4)
            elif i[0]>68:
                return 5
        
            
def ioj(i): #funkcja określająca w której wartości granicznej znajduje się indeks okrzemkowy
    if i[0]<0.15:
        return (5)
    elif 0.15<=i[0]<=0.4:
        return(4)
    elif 0.4<i[0]<=0.6:
        return (3)
    elif 0.6<i[0]<=0.8:
        return(2)
    elif i[0]>0.8:
        return (1)

def mise(i,typ): #funkcja określająca w której wartości granicznej znajduje się makrofitowy indeks stanu ekologicznego
    if typ=="2a" or typ=="3a" or typ=="5a" or typ=="6a" or typ=="7a":
        if i[0]>=0.68:
            return(1)
        if 0.68>i[0]>=0.34:
            return(2)
        if 0.34>i[0]>=0.17:
            return(3)
        if 0.17>i[0]>=0.09:
            return(4)
        if i[0]<0.09:
            return(5)
    if typ=="2b" or typ=="3b" or typ=="5b" or typ=="6b" or typ=="7b":
        if i[0]>=0.68:
            return(1)
        if 0.68>i[0]>=0.27:
            return(2)
        if 0.27>i[0]>=0.11:
            return(3)
        if 0.11>i[0]>=0.05:
            return(4)
        if i[0]<0.05:
            return(5)
    else:
        return (0)

#Funkcja określająca przynależność do klas elementów hydromorfologicznych
#jeżeli i=0 to znaczy że nie odpowiada warunkom niezakłóconym, jeżeli i=1 to odpowiada


def hydromorf(i): 
    if i[0]==1:
        return(1)
    else:
        return(0)

# dla funkcji poniżej dyrektywa klasyfikuje do 2 kategorii jednocześnie, spytać się co zrobić

def secchi(i,typ, schindler): #widzialność krążka secchiego
    if typ=='1a' or typ=='2a' or typ=='3a' or typ=='5a' or typ=='6a' or typ=='7a':
        if schindler<=2:
            if i[0]>=2.5:
                return (1)
            else:
                return(0)
        if schindler>2:
            if i[0]>=1.7:
                return (1)
            else:
                return(0)
    if typ=='1b' or typ=='2b' or typ=='3b' or typ=='4' or typ=='5b' or typ=='6b' or typ=='7b':
        if schindler<=2:
            if i[0]>=1.5:
                return (1)
            else:
                return(0)

        if schindler>2:
            if i[0]>=1:
                return (1)
            else:
                return(0)
    
def tlen1(i): #tlen rozpuszczony
    if i[0]>=4:
        return(1)
    else:
        return(0)

def tlen2(i): #nasycenie tlenem hypolimnionu
    if i[0]>=10:
        return(1)
    else:
        return(0)

def przew(i): #przewodność
    if i[0]<=600:
        return(1)
    else:
        return(0)

def azot(i,typ, schindler): #stężenie azotu całkowitego
    if typ=='1a' or typ=='2a' or typ=='3a' or typ=='5a' or typ=='6a' or typ=='7a':
        if schindler<=2:
            if i[0]<=1.5:
                return (1)
            else:
                return(0)
        if schindler>2:
            if i[0]<=2:
                return (1)
            else:
                return(0)
    if typ=='1b' or typ=='2b' or typ=='3b' or typ=='4' or typ=='5b' or typ=='6b' or typ=='7b':
        if schindler<=2:
            if i[0]<=1.6:
                return (1)
            else:
                return(0)

        if schindler>2:
            if i[0]<=2.5:
                return (1)
            else:
                return(0)


def fosfor(i,typ, schindler): #stężenie fosforu ogólnego
    if typ=='1a' or typ=='2a' or typ=='3a' or typ=='5a' or typ=='6a' or typ=='7a':
        if schindler<=2:
            if i[0]<=0.06:
                return (1)
            else:
                return(0)
        if schindler>2:
            if i[0]<=0.09:
                return (1)
            else:
                return(0)
    if typ=='1b' or typ=='2b' or typ=='3b' or typ=='4' or typ=='5b' or typ=='6b' or typ=='7b':
        if schindler<=2:
            if i[0]<=0.1:
                return (1)
            else:
                return(0)

        if schindler>2:
            if i[0]<=0.12:
                return (1)
            else:
                return(0)

########Tutaj zaczynają się wartości graniczne wskaźników jakości wód
########z grupy sobstancji szczególnie szkodliwych dla środowiska wodnego

def aldehyd(i):
    if i[0]<=0.05:
        return(1)
    else:
        return(0)
def arsen(i):
    if i[0]<=0.05:
        return(1)
    else:
        return(0)    
def bar(i):
    if i[0]<=0.5:
        return(1)
    else:
        return(0)
def bor(i):
    if i[0]<=2.:
        return(1)
    else:
        return(0)
def chrom6(i):
    if i[0]<=0.02:
        return(1)
    else:
        return(0)
def chrom(i):
    if i[0]<=0.05:
        return(1)
    else:
        return(0)
def cynk(i):
    if i[0]<=1:
        return(1)
    else:
        return(0)
def miedz(i):
    if i[0]<=0.05:
        return(1)
    else:
        return(0)
def I_F(i): #indeks fenolowy
    if i[0]<=0.01:
        return(1)
    else:
        return(0)
def IOM(i): #indeks oleju mineralnego
    if i[0]<=0.2:
        return(1)
    else:
        return(0)
def glin(i):
    if i[0]<=0.4:
        return(1)
    else:
        return(0)
def cyjankiw(i): #cyjanki wolne
    if i[0]<=0.05:
        return(1)
    else:
        return(0)
def cyjankiz(i): #cyjanki związane
    if i[0]<=0.05:
        return(1)
    else:
        return(0)
def molibden(i):
    if i[0]<=0.04:
        return(1)
    else:
        return(0)
def selen(i):
    if i[0]<=0.02:
        return(1)
    else:
        return(0)
def srebro(i):
    if i[0]<=0.005:
        return(1)
    else:
        return(0)
def tal(i):
    if i[0]<=0.002:
        return(1)
    else:
        return(0)
def tytan(i):
    if i[0]<=0.05:
        return(1)
    else:
        return(0)
def wanad(i):
    if i[0]<=0.05:
        return(1)
    else:
        return(0)
def antymon(i):
    if i[0]<=0.002:
        return(1)
    else:
        return(0)
def fluorki(i):
    if i[0]<=1.5:
        return(1)
    else:
        return(0)
def beryl(i):
    if i[0]<=0.0008:
        return(1)
    else:
        return(0)
def kobalt(i):
    if i[0]<=0.05:
        return(1)
    else:
        return(0)



def mean(x):
    temp=x.split(',')
    temp=[float(i) for i in temp]
    if len(temp)>1:
        return [sum(temp)/len(temp)]
    else:
        return temp



class MyForm(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)
                #MOJE FUNKCJE I POŁĄCZENIA
                QtCore.QObject.connect(self.ui.przycisk_klasyfikuj,QtCore.SIGNAL("clicked()"), self.start) #łączy przycisk klasyfikuj z funkcją start
                QtCore.QObject.connect(self.ui.action_open, QtCore.SIGNAL("triggered()"), self.wczytaj) #łączy przycisk Wczytaj raport z funkcją wczytaj
                QtCore.QObject.connect(self.ui.action_save, QtCore.SIGNAL("triggered()"), self.zapisz) #łączy przycisk Zapisz raport z funkcją zapisz
                QtCore.QObject.connect(self.ui.action_save_results, QtCore.SIGNAL("triggered()"), self.zapisz_wyniki) #łączy przycisk zapisz wyniki z funkcją zapisz_wyniki
                QtCore.QObject.connect(self.ui.action_author, QtCore.SIGNAL("triggered()"), self.o_autorze) #łączy przycick o autorze z funkcją o_autorze
                QtCore.QObject.connect(self.ui.action_about, QtCore.SIGNAL("triggered()"), self.o_programie)#łączy przycisk o programie z funkcją o_programie

        
            
        #FUNKCJE SŁUŻĄCE DO KLASYFIKACJI
        def start(self): #funkcja sczytująca dane z formularza i rozpoczynająca klasyfikację
            try:
                dane=[] #utworzenie listy z danymi
                
                typ=str((self.ui.typ.currentText())) #utworzenie zmiennej z typem jeziora, ta funkcja pobieraja dane z właściwości currentText QComboBox
                schindler=float((self.ui.schindler.text())) #utworzenie zmiennej ze współczynnikiem schindlera, tego typu funkcje pobierają dane z właściwości text QLineEdit

                #wskaźniki biologiczne
                
                dane.append(mean((str((self.ui.chlorofil.text()))))) #tutaj zawartość QLineBox jest przekazywana w formie ciągu znaków do funkcji mean
                dane.append(mean((str((self.ui.IOJ.text())))))
                dane.append(mean((str((self.ui.MISE.text())))))

                #Elementy hydromorfologiczne
                
                if self.ui.hydro1.isChecked()==True: #Sprawdzam czy w QCheckBox zaznaczono że jezioro ma klasę pierwszą, jeśli tak, to dodaję do listy danych 1, a jak nie to 0
                    dane.append([1])
                elif self.ui.hydro1.isChecked()==False:
                    dane.append([0])
                    
                if self.ui.hydro2.isChecked()==True:
                    dane.append([1])
                elif self.ui.hydro2.isChecked()==False:
                    dane.append([0])
                    
                if self.ui.hydro3.isChecked()==True:
                    dane.append([1])
                elif self.ui.hydro3.isChecked()==False:
                    dane.append([0])
                    
                if self.ui.morf1.isChecked()==True:
                    dane.append([1])
                elif self.ui.morf1.isChecked()==False:
                    dane.append([0])
                    
                if self.ui.morf2.isChecked()==True:
                    dane.append([1])
                elif self.ui.morf2.isChecked()==False:
                    dane.append([0])
                    
                if self.ui.morf3.isChecked()==True:
                    dane.append([1])
                elif self.ui.morf3.isChecked()==False:
                    dane.append([0])

                #Elementy fizykochemiczne
                    
                dane.append(mean((str((self.ui.secchi.text())))))
                dane.append(mean((str((self.ui.tlen1.text())))))
                dane.append(mean((str((self.ui.tlen2.text())))))
                dane.append(mean((str((self.ui.przew.text())))))
                dane.append(mean((str((self.ui.azot.text())))))
                dane.append(mean((str((self.ui.fosfor.text())))))

                #Zanieczyszczenia

                dane.append(mean((str((self.ui.aldehyd.text())))))
                dane.append(mean((str((self.ui.arsen.text())))))
                dane.append(mean((str((self.ui.bar.text())))))
                dane.append(mean((str((self.ui.bor.text())))))
                dane.append(mean((str((self.ui.chrom6.text())))))
                dane.append(mean((str((self.ui.chrom.text())))))
                dane.append(mean((str((self.ui.cynk.text())))))
                dane.append(mean((str((self.ui.miedz.text())))))
                dane.append(mean((str((self.ui.I_F.text())))))
                dane.append(mean((str((self.ui.IOM.text())))))
                dane.append(mean((str((self.ui.glin.text())))))
                dane.append(mean((str((self.ui.cyjankiw.text())))))
                dane.append(mean((str((self.ui.cyjankiz.text())))))
                dane.append(mean((str((self.ui.molibden.text())))))
                dane.append(mean((str((self.ui.selen.text())))))
                dane.append(mean((str((self.ui.srebro.text())))))              
                dane.append(mean((str((self.ui.tal.text())))))
                dane.append(mean((str((self.ui.tytan.text())))))
                dane.append(mean((str((self.ui.wanad.text())))))
                dane.append(mean((str((self.ui.antymon.text())))))
                dane.append(mean((str((self.ui.fluorki.text())))))
                dane.append(mean((str((self.ui.beryl.text())))))
                dane.append(mean((str((self.ui.kobalt.text())))))
                #Koniec wczytywania danych

                #Klasyfikowanie wskaźników według ramowej dyrektywy wodnej
                klasyfikacje=klasy(typ,schindler,dane)

                #Podział klasyfikacji na listę ze wskaźnikami i listę z zanieczyszczeniami

                wskazniki_biol=klasyfikacje[:3]
                wskazniki_hydromorf=klasyfikacje[3:9]
                wskazniki_fiz=klasyfikacje[9:15]
                zanieczyszczenia=klasyfikacje[15:]

                biol_el=max(wskazniki_biol)
                fiz_el=min(wskazniki_fiz)
                zan_el=min(zanieczyszczenia)

                klasa_jeziora=klas_jeziora (biol_el,fiz_el,zan_el)

                kolor=koloruj(klasa_jeziora)
                
                ### Funkcje piszące w okienku z wynikami
                
                self.ui.wyniki.clear()
                self.ui.wyniki.setTextBackgroundColor(QtGui.QColor('lightgray'))
                self.ui.wyniki.setTextColor(kolor)
                self.ui.wyniki.setFontUnderline(True)
                self.ui.wyniki.append('Klasa jeziora: '+klasa_jeziora)
                self.ui.wyniki.setFontUnderline(False)
                self.ui.wyniki.setTextColor(QtGui.QColor('black'))
                self.ui.wyniki.setTextBackgroundColor(QtGui.QColor('white'))
                
                self.ui.wyniki.append(u'\n##### Szczegóły #####\n')
                
                self.ui.wyniki.append(u'<u>##### Wskaźniki biologiczne #####</u>')
                
                self.ui.wyniki.append('\nChlorofil a: klasa '+str(wskazniki_biol[0]))
                self.ui.wyniki.append('IOJ: klasa '+str(wskazniki_biol[1]))

                if wskazniki_biol[2]!=0:
                    self.ui.wyniki.append('MISE: klasa '+str(wskazniki_biol[2]))
                else:
                    self.ui.wyniki.append(u'MISE: Wskaźnik nieuwzględniony')

                self.ui.wyniki.append('')
                self.ui.wyniki.append('<u>##### Elementy fizykochemiczne #####</u>')
                self.ui.wyniki.append('')
                
                self.ui.wyniki.append(u'Widzialnośc krazka Secchiego: '+przekroczenie(wskazniki_fiz[0]))
                self.ui.wyniki.append('Tlen rozpuszczony: '+przekroczenie(wskazniki_fiz[1]))
                self.ui.wyniki.append('Nasycenie tlenem hypolimnionu: '+przekroczenie(wskazniki_fiz[2]))
                self.ui.wyniki.append(u'Przewodność: '+przekroczenie(wskazniki_fiz[3]))
                self.ui.wyniki.append(u'Azot całkowity: '+przekroczenie(wskazniki_fiz[4]))
                self.ui.wyniki.append(u'Fosfor ogólny: '+przekroczenie(wskazniki_fiz[5]))

                self.ui.wyniki.append('')
                self.ui.wyniki.append(u'<u>##### Substancje szczególnie szkodliwe #####</u>')
                self.ui.wyniki.append('')
                
                self.ui.wyniki.append('Aldehyd: '+przekroczenie(zanieczyszczenia[0]))
                self.ui.wyniki.append('Arsen: '+przekroczenie(zanieczyszczenia[1]))
                self.ui.wyniki.append('Bar: '+przekroczenie(zanieczyszczenia[2]))
                self.ui.wyniki.append('Bor: '+przekroczenie(zanieczyszczenia[3]))
                self.ui.wyniki.append(u'Chrom sześciowartościowy: '+przekroczenie(zanieczyszczenia[4]))
                self.ui.wyniki.append(u'Chrom ogólny: '+przekroczenie(zanieczyszczenia[5]))
                self.ui.wyniki.append('Cynk: '+przekroczenie(zanieczyszczenia[6]))
                self.ui.wyniki.append(u'Miedź: '+przekroczenie(zanieczyszczenia[7]))
                self.ui.wyniki.append('Indeks fenolowy: '+przekroczenie(zanieczyszczenia[8]))
                self.ui.wyniki.append('Indeks oleju mineralnego: '+przekroczenie(zanieczyszczenia[9]))
                self.ui.wyniki.append('Glin: '+przekroczenie(zanieczyszczenia[10]))
                self.ui.wyniki.append('Cyjanki wolne: '+przekroczenie(zanieczyszczenia[11]))
                self.ui.wyniki.append(u'Cyjanki związane: '+przekroczenie(zanieczyszczenia[12]))
                self.ui.wyniki.append('Molibden: '+przekroczenie(zanieczyszczenia[13]))
                self.ui.wyniki.append('Selen: '+przekroczenie(zanieczyszczenia[14]))
                self.ui.wyniki.append('Srebro: '+przekroczenie(zanieczyszczenia[15]))
                self.ui.wyniki.append('Tal: '+przekroczenie(zanieczyszczenia[16]))
                self.ui.wyniki.append('Tytan: '+przekroczenie(zanieczyszczenia[17]))
                self.ui.wyniki.append('Wanad: '+przekroczenie(zanieczyszczenia[18]))
                self.ui.wyniki.append('Antymon: '+przekroczenie(zanieczyszczenia[19]))
                self.ui.wyniki.append('Fluorki: '+przekroczenie(zanieczyszczenia[20]))
                self.ui.wyniki.append('Beryl: '+przekroczenie(zanieczyszczenia[21]))
                self.ui.wyniki.append('Kobalt: '+przekroczenie(zanieczyszczenia[22]))                
                self.ui.wyniki.moveCursor(QtGui.QTextCursor.Start)
                
            except:
                QtGui.QMessageBox.warning(None,u'Błąd',u'Wprowadzono nieprawidłowe dane.')
                


        def zapisz_wyniki(self): #funkcja służąca do zapisywania zawartości okienka z wynikami klasyfikacji
            plik_raportu = QtGui.QFileDialog.getSaveFileName(self,'Zapisz plik jako...','wyniki','HTML (*.html)')
            if plik_raportu!='':
                try:
                    plik_raportu=codecs.open(plik_raportu,'w','cp1250') 
                    plik_raportu.write(unicode(self.ui.wyniki.toHtml())) 
                    plik_raportu.close()
                except:
                    QtGui.QMessageBox.warning(None,u'Błąd',u'Błąd zapisu.')
            
            
        def zapisz(self): #funkcja służąca do zapisywania pliku z wprowadzonymi danymi
            plik = QtGui.QFileDialog.getSaveFileName(self,'Zapisz plik jako...','dane','TXT (*.txt)') #okienko dialogowe pytające o miejsce zapisu
            if plik!='': #sprawdzenie czy użytkownik nie kliknął anuluj, jeżeli nie kliknął to następuje zapis
                try:
                    plik=open(plik,'w')
                    plik.write('typ="'+self.ui.typ.currentText()+'"\n')
                    plik.write('schindler="'+self.ui.schindler.text()+'"\n')
                    plik.write('chlorofil="'+self.ui.chlorofil.text()+'"\n')
                    plik.write('IOJ="'+self.ui.IOJ.text()+'"\n')
                    plik.write('MISE="'+self.ui.MISE.text()+'"\n')
                    if self.ui.hydro1.isChecked()==True: #Sprawdzam czy w QCheckBox zaznaczono że jezioro ma klasę pierwszą, jeśli tak, to dodaję do listy danych1, a jak nie to 0
                        plik.write('hydro1="1"\n')
                    elif self.ui.hydro1.isChecked()==False:
                        plik.write('hydro1="0"\n')
                        
                    if self.ui.hydro2.isChecked()==True:
                        plik.write('hydro2="1"\n')
                    elif self.ui.hydro2.isChecked()==False:
                        plik.write('hydro2="0"\n')
                        
                    if self.ui.hydro3.isChecked()==True:
                        plik.write('hydro3="1"\n')
                    elif self.ui.hydro3.isChecked()==False:
                        plik.write('hydro3="0"\n')
                    
                    if self.ui.morf1.isChecked()==True:
                        plik.write('morf1="1"\n')
                    elif self.ui.morf1.isChecked()==False:
                        plik.write('morf1="0"\n')
                        
                    if self.ui.morf2.isChecked()==True:
                        plik.write('morf2="1"\n')
                    elif self.ui.morf2.isChecked()==False:
                        plik.write('morf2="0"\n')
                        
                    if self.ui.morf3.isChecked()==True:
                        plik.write('morf3="1"\n')
                    elif self.ui.morf3.isChecked()==False:
                        plik.write('morf3="0"\n')
                        
                    plik.write('secchi="'+self.ui.secchi.text()+'"\n')
                    plik.write('tlen1="'+self.ui.tlen1.text()+'"\n')
                    plik.write('tlen2="'+self.ui.tlen2.text()+'"\n')
                    plik.write('przew="'+self.ui.przew.text()+'"\n')
                    plik.write('azot="'+self.ui.azot.text()+'"\n')
                    plik.write('fosfor="'+self.ui.fosfor.text()+'"\n')

                    plik.write('aldehyd="'+self.ui.aldehyd.text()+'"\n')
                    plik.write('arsen="'+self.ui.arsen.text()+'"\n')
                    plik.write('bar="'+self.ui.bar.text()+'"\n')
                    plik.write('bor="'+self.ui.bor.text()+'"\n')
                    plik.write('chrom6="'+self.ui.chrom6.text()+'"\n')
                    plik.write('chrom="'+self.ui.chrom.text()+'"\n')
                    plik.write('cynk="'+self.ui.cynk.text()+'"\n')
                    plik.write('miedź="'+self.ui.miedz.text()+'"\n')
                    plik.write('I_F="'+self.ui.I_F.text()+'"\n')
                    plik.write('IOM ="'+self.ui.IOM .text()+'"\n')
                    plik.write('glin="'+self.ui.glin.text()+'"\n')
                    plik.write('cyjankiw ="'+self.ui.cyjankiw.text()+'"\n')
                    plik.write('cyjankiz ="'+self.ui.cyjankiz.text()+'"\n')
                    plik.write('molibden="'+self.ui.molibden.text()+'"\n')
                    plik.write('selen="'+self.ui.selen.text()+'"\n')
                    plik.write('srebro="'+self.ui.srebro.text()+'"\n')
                    plik.write('tal="'+self.ui.tal.text()+'"\n')
                    plik.write('tytan="'+self.ui.tytan.text()+'"\n')
                    plik.write('wanad="'+self.ui.wanad.text()+'"\n')
                    plik.write('antymon="'+self.ui.antymon.text()+'"\n')
                    plik.write('fluorki="'+self.ui.fluorki.text()+'"\n')
                    plik.write('beryl="'+self.ui.beryl.text()+'"\n')
                    plik.write('kobalt="'+self.ui.kobalt.text()+'"\n')
                               
                    plik.close()
                except:
                    QtGui.QMessageBox.warning(None,u'Błąd',u'Błąd zapisu.')

        def wczytaj(self): #funkcja służąca do wczytywania
            
            plik = QtGui.QFileDialog.getOpenFileName(self,'Wybierz plik z raportem','','TXT (*.txt)')
            if plik!='':
                try:
                    plik=open(plik,'r')
                    plik_lista=[]
                    for line in plik:
                        i=line.find('"')
                        if i<>-1:
                            n=line[i+1:].find('"')
                            plik_lista.append(line[i+1:n+i+1])
                    plik.close()
                    self.ui.schindler.setText(plik_lista[1])
                    self.ui.chlorofil.setText(plik_lista[2])
                    self.ui.IOJ.setText(plik_lista[3])
                    self.ui.MISE.setText(plik_lista[4])
                    
                    self.ui.secchi.setText(plik_lista[11])
                    self.ui.tlen1.setText(plik_lista[12])
                    self.ui.tlen2.setText(plik_lista[13])
                    self.ui.przew.setText(plik_lista[14])
                    self.ui.azot.setText(plik_lista[15])
                    self.ui.fosfor.setText(plik_lista[16])

                    self.ui.aldehyd.setText(plik_lista[17])
                    self.ui.arsen.setText(plik_lista[18])
                    self.ui.bar.setText(plik_lista[19])
                    self.ui.bor.setText(plik_lista[20])
                    self.ui.chrom6.setText(plik_lista[21])
                    self.ui.chrom.setText(plik_lista[22])
                    self.ui.cynk.setText(plik_lista[23])
                    self.ui.miedz.setText(plik_lista[24])
                    self.ui.I_F.setText(plik_lista[25])
                    self.ui.IOM.setText(plik_lista[26])
                    self.ui.glin.setText(plik_lista[27])
                    self.ui.cyjankiw.setText(plik_lista[28])
                    self.ui.cyjankiz.setText(plik_lista[29])
                    self.ui.molibden.setText(plik_lista[30])
                    self.ui.selen.setText(plik_lista[31])
                    self.ui.tal.setText(plik_lista[33])
                    self.ui.srebro.setText(plik_lista[32])
                    self.ui.tytan.setText(plik_lista[34])
                    self.ui.wanad.setText(plik_lista[35])
                    self.ui.antymon.setText(plik_lista[36])
                    self.ui.fluorki.setText(plik_lista[37])
                    self.ui.beryl.setText(plik_lista[38])
                    self.ui.kobalt.setText(plik_lista[39])

                    self.ui.typ.setCurrentIndex(self.ui.typ.findText(plik_lista[0])) #linijka ustawia typ jeziora, funkcja findText wyszukuje, a setcurrentomdex ustawia

                    
                    if int(plik_lista[5])==1:
                        self.ui.hydro1.setChecked(True)
                    elif int(plik_lista[5])==0:
                        self.ui.hydro1.setChecked(False)

                    if int(plik_lista[6])==1:
                        self.ui.hydro2.setChecked(True)
                    elif int(plik_lista[6])==0:
                        self.ui.hydro2.setChecked(False)

                    if int(plik_lista[7])==1:
                        self.ui.hydro3.setChecked(True)
                    elif int(plik_lista[7])==0:
                        self.ui.hydro3.setChecked(False)

                    if int(plik_lista[8])==1:
                        self.ui.morf1.setChecked(True)
                    elif int(plik_lista[8])==0:
                        self.ui.morf1.setChecked(False)

                    if int(plik_lista[9])==1:
                        self.ui.morf2.setChecked(True)
                    elif int(plik_lista[9])==0:
                        self.ui.morf2.setChecked(False)

                    if int(plik_lista[10])==1:
                        self.ui.morf3.setChecked(True)
                    elif int(plik_lista[10])==0:
                        self.ui.morf3.setChecked(False)
                    

                
                except:
                    QtGui.QMessageBox.warning(None,u'Błąd',u'Plik ma niewłaściwy format.')
                    
        def o_autorze(self): #funkcja wyświetlająca informacje o autorze programu
            QtGui.QMessageBox.information(None,u'Autor',u'Autor: Damian Kacperski\nUczelnia: Uniwersytet Przyrodniczy we Wrocławiu\nKierunek: Bioinformatyka\nWrocław, 2014')

        def o_programie(self): #funkcja wyświetlająca informacje o programie i mówiąca jak wpisywać dane
            QtGui.QMessageBox.information(None,u'O programie',u'Program służy do klasyfikacji jezior zgodnie z Ramową Dyrektywą Wodną, czyli według rozporządzenia Ministra Środowiska z dnia 9 listopada 2011 r. w sprawie sposobu klasyfikacji stanu jednolitych części wód powierzchniowych oraz środowiskowych norm jakości dla substancji priorytetowych.\nProgram powstał jako praca licencjacka w zakładzie Hydrobiologii i Akwakultury\nUniwersytetu Przyrodniczego we Wrocławiu.\n\nDane należy wprowadzać w okienka, separatorem dziesiętnym musi być kropka, przecinek oddziela pomiary, program automatycznie policzy średnią z pomiarów. Cyna nie została uwzględniona, gdyż warunki referencyjne dla niej są wciąż ustalane. Elementy hydromorfologiczne także nie są brane pod uwagę w ocenie, gdyż rozporządzenie jeszcze ich nie uwzględnia, jedenak wciąż możliwe jest zaznaczenie czy spełniają warunki referencyjne, co pozwoli na zachowanie tych danych do pliku.') 
                                          
             
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())


	  
