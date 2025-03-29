from tkinter import *

from interface.frame_sudoku import FrameSudoku
from interface.frame_outils import FrameOutils

from algorithme.algorithme import Algorithme
from algorithme.sauvegarde_sudoku import SauvegadeSudoku



class Root(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("1200x600+0+0")
        self.configure(bg="grey50")

        self.frame_sudoku=FrameSudoku(self)
        self.frame_sudoku.grid(row=0,column=0,padx=5,pady=5)

        self.frame_outils=FrameOutils(self)
        self.frame_outils.grid(row=0,column=1)

        self.algo=Algorithme(self)
        self.sauvegarde_sudoku=SauvegadeSudoku(self)

        self.charger()

    def charger(self):
        self.sudoku_actif=self.sauvegarde_sudoku.sudoku_moyen
        self.frame_sudoku.print_all(self.sudoku_actif, self.sudoku_actif)
        board_possible = self.algo.cherche_possible(self.sudoku_actif)
        self.frame_sudoku.print_all_infos(board_possible)

    def clear(self):
        self.frame_sudoku.clear()
        sudoku = self.frame_sudoku.get_board()
        board_possible = self.algo.cherche_possible(sudoku)
        self.frame_sudoku.print_all_infos(board_possible)

    def valide(self):
        sudoku = self.frame_sudoku.get_board()
        rep=self.algo.isvalide(sudoku)
        print(rep)

    def key_press_sudoku(self,event):
        self.frame_sudoku.modify_space_before_draw(event)
        sudoku = self.frame_sudoku.get_board()
        board_possible = self.algo.cherche_possible(sudoku)
        self.frame_sudoku.print_all_infos(board_possible)

    def cherche_possible(self):
        sudoku=self.frame_sudoku.get_board()
        board_possible=self.algo.cherche_possible(sudoku)
        self.frame_sudoku.print_all_infos(board_possible)

    def recherche_simple(self):
        sudoku = self.frame_sudoku.get_board()
        sudoku = self.algo.recherche_simple(sudoku)
        board_possible = self.algo.cherche_possible(sudoku)
        self.frame_sudoku.print_all(sudoku, self.sudoku_actif)
        self.frame_sudoku.print_all_infos(board_possible)

if __name__=="__main__":
    root=Root()
    root.mainloop()

