import tkinter as tk
import os
def kreatormap():
    #Funkcja obsługująca kreator map
    def export(*args):
        #Zapis mapy do pliku .txt
        f=open(os.getcwd()+"\Mapy\%s.txt"%nazwa.get(),"w")
        f.write(str(xsize.get())+";"+str(xsize.get())+";"+str(mapa)+";"+str(["....."]*10)+";"+str(["0"]*10))
        f.close()
    def checknr(arg,*args):
        #Sprawdzanie numeru klikniętego przycisku
        #Działa dla Python3.6.5, dla wcześniejszych tkinter jest niekompatybilny
        x=0
        if(str(arg)[-1]=="n"):
            x=1
        elif(str(arg)[-2]=="n"):
            x=int(str(arg)[-1])
        elif(str(arg)[-3]=="n"):
            x=int(str(arg)[-1])+10*int(str(arg)[-2])
        elif(str(arg)[-4]=="n"):
            x=int(str(arg)[-1])+10*int(str(arg)[-2])+100*int(str(arg)[-3])
        elif(str(arg)[-5]=="n"):
            x=int(str(arg)[-1])+10*int(str(arg)[-2])+100*int(str(arg)[-3])+1000*int(str(arg)[-4])
        return x

    def zmien(arg,*args):
        #Zamiana koloru przycisku na odpowiadający odpowiedniemu obiektowi
        x=checknr(arg)
        if (tryb.get()==1):
            arg.config(bg = 'blue') #ściana
        elif (tryb.get()==2):
            arg.config(bg = 'magenta') #punkt
        elif (tryb.get()==3):
            arg.config(bg = 'purple') #powerup
        elif (tryb.get()==4):
            arg.config(bg = 'red') #duch1-blinky
            inmap(tryb.get())
        elif (tryb.get()==5):
            arg.config(bg = 'pink') #duch2-pinky
            inmap(tryb.get())
        elif (tryb.get()==6):
            arg.config(bg = 'cyan') #duch3-inky
            inmap(tryb.get())
        elif (tryb.get()==7):
            arg.config(bg = 'orange') #duch4-clyde
            inmap(tryb.get())
        elif (tryb.get()==8):
            arg.config(bg = 'yellow') #pacman
            inmap(tryb.get())
        mapa[x-1]=tryb.get()

    def inmap(n,*args):
        #Usuwanie obiektów które mogą wystąpić tylko raz na planszy
        if n in mapa:
            tiles[mapa.index(n)].config(bg = 'magenta')
            mapa[mapa.index(n)]=2
    def wypelnij(*args):
        #Wypełnienie mapy obiektami punktu
        for i in range(len(mapa)):
            if(mapa[i]==0):
                mapa[i]=2
                tiles[i].config(bg = 'magenta')
    def szkic(*args):
        #Szkicowanie listy przechowującej mapę
        global mapa
        mapa=[0]*xsize.get()*xsize.get()
        return mapa

    def rysuj(*args):
        #Rysowanie mapy z przyciskó
        szkic()
        global tiles
        global buttons
        try:
            clear()
        except:
            pass
        buttons=tk.Frame(ramka) #Ramka z przyciskami
        buttons.grid(column=10, row = 3)
        tiles=[0]*xsize.get()*xsize.get() #Lista wszystkich przycisków
        while (str(xsize.get())[0]==0): 
            #Ignorowanie cyfr 0 występujących przed liczbą, zapobiega konwersji do systemu ósemkowego
            xsize.set(str(xsize.get()[1:]))
        for j in range(xsize.get()):
            for i in range(xsize.get()):
                if(i==0 or j==0 or i==xsize.get()-1 or j==xsize.get()-1):
                    tiles[i+(xsize.get())*j]=tk.Button(buttons,image=pixel,bg = 'blue')
                    tiles[i+(xsize.get())*j].config(command = lambda arg = tiles[i+(xsize.get())*j]: zmien(arg))
                    tiles[i+(xsize.get())*j].grid(column=i ,row = j)
                    mapa[i+(xsize.get())*j]=1
                else:
                    tiles[i+(xsize.get())*j]=tk.Button(buttons,image=pixel,bg = 'white')
                    tiles[i+(xsize.get())*j].config(command = lambda arg = tiles[i+(xsize.get())*j]: zmien(arg))
                    tiles[i+(xsize.get())*j].grid(column=i ,row = j)
    def zmientryb(n,*args):
        #Zmiana aktywnego obiektu do rysowania
        if n==1:
            tryb.set(1)
        elif n==2:
            tryb.set(2)
        elif n==3:
            tryb.set(3)
        elif n==4:
            tryb.set(4)
        elif n==5:
            tryb.set(5)
        elif n==6:
            tryb.set(6)
        elif n==7:
            tryb.set(7)
        elif n==8:
            tryb.set(8)
        elif n==8:
            tryb.set(9)
    def clear(*args):
        #Czyszczenie ramki z przyciskami
        for i in range(len(tiles)-1,-1,-1):
            tiles[i].destroy()
        buttons.delete()
    #GUI
    top=tk.Tk() 
    pixel = tk.PhotoImage(width=8, height=8)
    top.title("Kreator map do gry PacMan")
    ramka=tk.Frame(top)
    ramka.grid(column=0,row=0)
    xsize=tk.IntVar(ramka)
    xsize.set(20)
    tryb=tk.IntVar(ramka)
    nazwa=tk.StringVar(ramka)
    nazwa.set("nazwa")
    tryb.set(1)

    l_wymiar=tk.Label(ramka,text="Wpisz rozmiar mapy: ")
    l_wymiar.grid(column=1,row=1)

    e_xsize=tk.Entry(ramka,width=8,textvariable=xsize)
    e_xsize.grid(column=2,row = 1)


    b_rysuj=tk.Button(ramka, text = "rysuj", command = rysuj)
    b_rysuj.grid(column= 5, row = 1)

    b_zapisz=tk.Button(ramka, text =  "zapisz",command = export)
    b_zapisz.grid(column=6, row = 1)

    b_sciana=tk.Button(ramka,text = "ściana",bg = 'blue', command = lambda: zmientryb(1))
    b_sciana.grid(column=2, row = 2)

    b_punkt=tk.Button(ramka,text = "punkt",bg = 'magenta', command = lambda: zmientryb(2))
    b_punkt.grid(column=3, row = 2)

    b_powerup=tk.Button(ramka,text = "specjal",bg = 'purple', command = lambda: zmientryb(3))
    b_powerup.grid(column=4, row = 2)

    b_duch1=tk.Button(ramka, text = "blinky",bg = 'red', command = lambda: zmientryb(4))
    b_duch1.grid(column=5, row = 2)

    b_duch2=tk.Button(ramka, text = "pinky",bg = 'pink',command = lambda: zmientryb(5))
    b_duch2.grid(column=6, row = 2)

    b_duch3=tk.Button(ramka,text = "inky",bg = 'cyan', command = lambda: zmientryb(6))
    b_duch3.grid(column=7, row = 2)

    b_duch4=tk.Button(ramka,text = "clyde",bg = 'orange', command = lambda: zmientryb(7))
    b_duch4.grid(column=8, row = 2)

    b_pacman=tk.Button(ramka,text = "pacman",bg = 'yellow', command = lambda: zmientryb(8))
    b_pacman.grid(column=8, row = 1)

    b_wypelnij=tk.Button(ramka,text = "wypelnij",bg = 'magenta', command = wypelnij)
    b_wypelnij.grid(column=7, row = 1)

    e_nazwa=tk.Entry(ramka, text = nazwa, textvariable=nazwa)
    e_nazwa.grid(column=1, row = 2)

    top.mainloop()