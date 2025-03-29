

class Algorithme:
    def __init__(self,boss):
        self.boss=boss

    def isvalide(self,board):
        for n in range(9):
            l=set(board[n])
            if len(l)<9:
                return False
        return True

    def cherche_possible(self,board):
        board_possible=[[[] for x in range(9)] for y in range(9)]
        for y in range(9):
            for x in range(9):
                board_possible[y][x]=self.cherche_possible_une_case(board,[x,y])
        return board_possible

    def cherche_possible_une_case(self,board,case):
        possible=['1','2','3','4','5','6','7','8','9']
        if board[case[1]][case[0]]!=".":
            return []
        for n in range(9):
            if board[n][case[0]] in possible:
                del possible[possible.index(board[n][case[0]])]
            if board[case[1]][n] in possible:
                del possible[possible.index(board[case[1]][n])]
        x1=(case[0]//3)*3
        y1=(case[1]//3)*3
        for y in range(3):
            for x in range(3):
                if board[y+y1][x+x1] in possible:
                    del possible[possible.index(board[y+y1][x+x1])]
        return possible

    def recherche_simple(self,board):
        liste_possible=self.cherche_possible(board)
        for y in range(9):
            for x in range(9):
                if len(liste_possible[y][x])==1:
                    board[y][x]=liste_possible[y][x][0]
        return board
