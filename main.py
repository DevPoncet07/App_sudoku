from tkinter import *

from interface.frame_sudoku import FrameSudoku
from interface.frame_outils import FrameOutils



class Root(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("600x600+0+0")
        self.configure(bg="grey50")

        self.frame_sudoku=FrameSudoku(self)
        self.frame_sudoku.grid(row=0,column=0,padx=5,pady=5)

        self.frame_outils=FrameOutils(self)
        self.frame_outils.grid(row=0,column=1)

    def clear(self):
        self.frame_sudoku.clear()

if __name__=="__main__":
    root=Root()
    root.mainloop()

