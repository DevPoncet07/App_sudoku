from tkinter import *


class FrameOutils(Frame):
    def __init__(self,boss):
        self.boss=boss
        Frame.__init__(self,master=boss,bg='grey50')

        self.boutton_charger=Button(self,text='Charger',command=self.boss.charger)
        self.boutton_charger.grid(row=0,column=0)

        self.boutton_clear=Button(self,text='Clear',command=self.boss.clear)
        self.boutton_clear.grid(row=1,column=0,pady=10)

        self.boutton_valide = Button(self, text='Valide', command=self.boss.valide)
        self.boutton_valide.grid(row=2, column=0)

        self.boutton_cherche_possible = Button(self, text='Cherche possible', command=self.boss.cherche_possible)
        self.boutton_cherche_possible.grid(row=3, column=0,pady=10)

        self.boutton_recherche_simple = Button(self, text='Recherche simple', command=self.boss.recherche_simple)
        self.boutton_recherche_simple.grid(row=4, column=0)