
from tkinter import *



class FrameSudoku(Frame):
    def __init__(self,boss):
        self.boss=boss
        Frame.__init__(self,master=boss)

        self.font_sudoku="verdana 30"
        self.font_info="verdana 10"
        if True:
        	self.font_sudoku="verdana 12"
        	self.font_info="verdana 4"
        	

        self.frame_sudoku=Frame(self,width=535,height=535,bg='grey30')
        self.frame_sudoku.pack(side=LEFT)
        self.frame_infos = Frame(self, width=535, height=535, bg='grey30')
        self.frame_infos.pack(side=RIGHT)


        self.entrys=[[None for x in range(9)]for y in range(9)]
        self.str_entrys=[[StringVar() for x in range(9)]for y in range(9)]
        self.infos = [[Canvas(self.frame_infos,width=50,height=50) for x in range(9)] for y in range(9)]
        self.str_infos = [[[] for x in range(9)] for y in range(9)]
        x1=8
        y1=8
        for y in range(9):
            x1=8
            for x in range(9):
                self.entrys[y][x] = Entry(self.frame_sudoku,width=2,textvariable=self.str_entrys[y][x],font=self.font_sudoku)
                self.entrys[y][x].bind("<KeyRelease>",self.boss.key_press_sudoku)
                self.entrys[y][x].place(x=x1,y=y1)
                self.infos[y][x].place(x=x1,y=y1)
                if (1+x)%3==0 and x>0:
                    x1+=8
                x1 += 56
            if (1+y)%3==0 and y>0:
                y1+=8
            y1 += 56

    def modify_space_before_draw(self,event):
        var=event.widget
        var.delete(0,END)
        var.insert(0," "+event.char)


    def clear(self):
        for y in range(9):
            for x in range(9):
                self.str_entrys[y][x].set("")

    def get_board(self):
        board=[]
        for y in range(9):
            ligne=[]
            for x in range(9):
                txt=self.str_entrys[y][x].get()
                if len(txt)>1:
                    ligne.append(txt[1])
                else:
                    ligne.append(".")
            board.append(ligne)
        return board

    def print_all(self,board,board_base):
        for y in range(9):
            for x in range(9):
                if board_base[y][x]==".":
                    self.entrys[y][x].configure(fg="blue")
                    if board[y][x]!=".":
                        self.str_entrys[y][x].set(" " + board[y][x])
                    else:
                        self.str_entrys[y][x].set("")
                else:
                    self.entrys[y][x].configure(fg="black")
                    self.str_entrys[y][x].set(" "+board[y][x])

    def print_all_infos(self,board):
        for y in range(9):
            for x in range(9):
                self.print_une_info(self.infos[y][x],board[y][x])


    def print_une_info(self,can,possible):
        can.delete(ALL)
        for e in possible:
            if e =="1":
                can.create_text(7,7,text=e,font=self.font_info)
            elif e =="2":
                can.create_text(27,7,text=e,font=self.font_info)
            elif e =="3":
                can.create_text(47,7,text=e,font=self.font_info)
            elif e =="4":
                can.create_text(7,27,text=e,font=self.font_info)
            elif e =="5":
                can.create_text(27,27,text=e,font=self.font_info)
            elif e =="6":
                can.create_text(47,27,text=e,font=self.font_info)
            elif e =="7":
                can.create_text(7,47,text=e,font=self.font_info)
            elif e =="8":
                can.create_text(27,47,text=e,font=self.font_info)
            elif e =="9":
                can.create_text(47,47,text=e,font=self.font_info)

