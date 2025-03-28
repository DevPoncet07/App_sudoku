from tkinter import *


class FrameOutils(Frame):
    def __init__(self,boss):
        self.boss=boss
        Frame.__init__(self,master=boss)
        self.boutton_clear=Button(self,text='Clear',command=self.boss.clear)
        self.boutton_clear.grid(row=0,column=0)