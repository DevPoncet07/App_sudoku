
from tkinter import *



class FrameSudoku(Frame):
    def __init__(self,boss):
        self.boss=boss
        Frame.__init__(self,master=boss,width=535,height=535,bg='grey30')

        self.entrys=[[None for x in range(9)]for y in range(9)]
        self.str_entrys=[[StringVar() for x in range(9)]for y in range(9)]
        x1=8
        y1=8
        for y in range(9):
            x1=8
            for x in range(9):
                self.entrys[y][x] = Entry(self,width=2,textvariable=self.str_entrys[y][x],font="Verdana 30",)
                self.entrys[y][x].bind("<Key>",self.modify_space_before_draw)
                self.entrys[y][x].place(x=x1,y=y1)
                if (1+x)%3==0 and x>0:
                    x1+=8
                x1 += 56
            if (1+y)%3==0 and y>0:
                y1+=8
            y1 += 56

    def modify_space_before_draw(self,event):
        print(event)
        var=event.widget
        var.delete(0,END)
        var.insert(0," ")

    def clear(self):
        for y in range(9):
            for x in range(9):
                self.str_entrys[y][x].set("")
