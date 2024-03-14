from itertools import product
from figure import figure

class board():
    def __init__(self) -> None:
        self.board={tuple(i): None for i in 
                    list(product([i for i in range(8)], [i for i in range(8)]))}
        for i in range(8):
            self.board[(i, 1)] = figure(self, "white", "P", (i, 1))  # Пешки белых на седьмом столбце
            self.board[(i, 6)] = figure(self, "black", "P", (i, 6))  # Пешки черных на втором столбце

        self.board[(0, 0)] = figure(self, "white", "R", (0, 0))  # Белая ладья на позиции a1
        self.board[(1, 0)] = figure(self, "white", "N", (1, 0))  # Белый конь на позиции b1
        self.board[(2, 0)] = figure(self, "white", "B", (2, 0))  # Белый слон на позиции c1
        self.board[(3, 0)] = figure(self, "white", "Q", (3, 0))  # Белая королева на позиции d1
        self.board[(4, 0)] = figure(self, "white", "K", (4, 0))  # Белый король на позиции e1
        self.board[(5, 0)] = figure(self, "white", "B", (5, 0))  # Белый слон на позиции f1
        self.board[(6, 0)] = figure(self, "white", "N", (6, 0))  # Белый конь на позиции g1
        self.board[(7, 0)] = figure(self, "white", "R", (7, 0))  # Белая ладья на позиции h1

        self.board[(0, 7)] = figure(self, "black", "R", (0, 7))  # Черная ладья на позиции a8
        self.board[(1, 7)] = figure(self, "black", "N", (1, 7))  # Черный конь на позиции b8
        self.board[(2, 7)] = figure(self, "black", "B", (2, 7))  # Черный слон на позиции c8
        self.board[(3, 7)] = figure(self, "black", "Q", (3, 7))  # Черная королева на позиции d8
        self.board[(4, 7)] = figure(self, "black", "K", (4, 7))  # Черный король на позиции e8
        self.board[(5, 7)] = figure(self, "black", "B", (5, 7))  # Черный слон на позиции f8
        self.board[(6, 7)] = figure(self, "black", "N", (6, 7))  # Черный конь на позиции g8
        self.board[(7, 7)] = figure(self, "black", "R", (7, 7))  # Черная ладья на позиции h8

    def move(self,move):
        if move=="0-0":
            pass
        elif move=="0-0":
            pass
        elif move=="0-0-0":
            pass
        elif "=" in move:
            pass
        fig,old_hor,old_ver,new_hor,new_ver=move[0],move[1],int(move[2]),move[3],int(move[4])
        decode={i[0]:i[1] for i in list(zip(list("abcdefgh"),[i for i in range(7)]))}

        old_hor_decode=decode[old_hor]
        new_hor_decode=decode[new_hor]
        old_ver_decode=old_ver-1
        new_ver_decode=new_ver-1

        if fig!=self.board[(old_hor_decode,old_ver_decode)].name:
            print(fig)
            print(self.board[(old_hor_decode,old_ver_decode)].name)
            raise KeyError(f"on {old_hor}{old_ver} not a {fig}")
            

        self.board[(old_hor_decode,old_ver_decode)].move((new_hor_decode,new_ver_decode))

    def __repr__(self) -> str:
        s=""
        for i in range(7,-1,-1):
            for j in range(7,-1,-1):
                if self.board[(i,j)]==None:
                    s+="--"+" "
                elif self.board[(i,j)].color=="white":
                    s+=f"w{self.board[(i,j)].name}"+" "
                elif self.board[(i,j)].color=="black":
                    s+=f"b{self.board[(i,j)].name}"+" "
            s+="\n"
        return s


b=board()

print(b)

b.move("Pa2a4")

print(b)