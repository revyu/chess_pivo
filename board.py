from itertools import product
from figure import figure
from typing import Tuple

class board():
    def __init__(self) -> None:
        self.board={tuple(i): None for i in # клетка - к фигуре
                    list(product([i for i in range(8)], [i for i in range(8)]))}
        for i in range(8):
            self.board[(1, i)] = figure(self, "white", "P", (1, i))  # Пешки белых на седьмом столбце
            self.board[(6, i)] = figure(self, "black", "P", (6, i))  # Пешки черных на втором столбце

        self.board[(0, 0)] = figure(self, "white", "R", (0, 0))  # Белая ладья на позиции a1
        self.board[(0, 1)] = figure(self, "white", "N", (0, 1))  # Белый конь на позиции b1
        self.board[(0, 2)] = figure(self, "white", "B", (0, 2))  # Белый слон на позиции c1
        self.board[(0, 3)] = figure(self, "white", "Q", (0, 3))  # Белая королева на позиции d1
        self.board[(0, 4)] = figure(self, "white", "K", (0, 4))  # Белый король на позиции e1
        self.board[(0, 5)] = figure(self, "white", "B", (0, 5))  # Белый слон на позиции f1
        self.board[(0, 6)] = figure(self, "white", "N", (0, 6))  # Белый конь на позиции g1
        self.board[(0, 7)] = figure(self, "white", "R", (0, 7))  # Белая ладья на позиции h1

        self.board[(7, 0)] = figure(self, "black", "R", (7, 0))  # Черная ладья на позиции a8
        self.board[(7, 1)] = figure(self, "black", "N", (7, 1))  # Черный конь на позиции b8
        self.board[(7, 2)] = figure(self, "black", "B", (7, 2))  # Черный слон на позиции c8
        self.board[(7, 3)] = figure(self, "black", "Q", (7, 3))  # Черная королева на позиции d8
        self.board[(7, 4)] = figure(self, "black", "K", (7, 4))  # Черный король на позиции e8
        self.board[(7, 5)] = figure(self, "black", "B", (7, 5))  # Черный слон на позиции f8
        self.board[(7, 6)] = figure(self, "black", "N", (7, 6))  # Черный конь на позиции g8
        self.board[(7, 7)] = figure(self, "black", "R", (7, 7))  # Черная ладья на позиции h8

        self.figures_dict={ # фигура- к клетке
            # точнее фигура к нескольким клеткам т.к. есть одинаковые фигуры на доске
            # создан что бы при подсчете шаха не перебирать все клетки доски
            # а только фигуры, более того только фигуры определенного цвета
            "white":{
                "P":[[1,i] for i in range(8)],
                "R":[[0,0],[0,7]],
                "N":[[0,1],[0,6]],
                "B":[[0,2],[0,5]],
                "Q":[[0,3]],
                "K":[[0,4]]
            },
            "black":{
                "P":[[6,i] for i in range(8)],
                "R":[[7,0],[7,7]],
                "N":[[7,1],[7,6]],
                "B":[[7,2],[7,5]],
                "Q":[[7,3]],
                "K":[[7,4]]
            }
        }


    def move(self,move):
        if move=="0-0":
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

        return self.board
    

    def get_all_moves(self, coordinates: Tuple):
        name = self.board[coordinates].name
        x = coordinates[0]
        y = coordinates[1]

        possible_moves = []

        if name == "P":
            if self.board[coordinates].color=="white":
                # тут может быть еще на самом деле en-passant но мне похрен его реализовывать
                # превращение пешки тоже будет реализовывать другой скрипт
                if y==1 and self.board[(x,2)]==None and self.board(x,3)==None:
                    possible_moves=[(x,2),(x,3)]
                elif self.board[(x,y+1)]!=None: 
                    possible_moves=[(x,y+1)]
            else:
                if y==7 and self.board[(x,6)]==None and self.board(x,5)==None:
                    possible_moves=[(x,6),(x,5)]
                elif self.board[(x,y-1)]!=None: 
                    possible_moves=[(x,y-1)]

        if name == "K":
            possible_moves = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]

        if name == "N":
            possible_moves = [(x - 2, y + 1), (x - 1, y + 2), (x + 1, y + 2), (x + 2, y + 1), (x + 2, y - 1), (x + 1, y - 2), (x - 1, y - 2), (x - 2, y - 1)]

        if name == "R" or name=="Q":
            
            x_copy = x

            # двигаемся влево пока на наших полях None и пока мы не вышли за пределы доски
            while (x_copy >= 0) and (self.board[(x_copy, y)] == None):
                x_copy -= 1
                possible_moves.append((x_copy, y))
                

            # вправо
            x_copy = x
            while (x_copy <= 7) and (self.board[(x_copy, y)] == None):
                x_copy += 1
                possible_moves.append((x_copy, y))
            

            # вверх
            y_copy = y
            while (y_copy <= 7) and (self.board[(x, y_copy)] == None):
                y_copy += 1
                possible_moves.append((x_copy, y))
              

            # вниз
            y_copy = y
            while (y_copy >= 0) and (self.board[(x, y_copy)] == None):
                y_copy -= 1
                possible_moves.append((x_copy, y))
                


        if name == "B" or name=="Q":
            
            x_copy = x
            y_copy = y

            # влево вниз
            while (x_copy >= 0) and (y_copy >= 0) and (self.board[(x_copy, y)] == None):
                x_copy -= 1
                y_copy -= 1
                possible_moves.append((x_copy, y_copy))
                

            x_copy = x
            y_copy = y

            # вправо вниз
            while (x_copy <= 7) and (y_copy>=0 ) and (self.board[(x_copy, y)] == None):
                possible_moves.append((x_copy, y))
                x_copy += 1
                y_copy -=1
            
            x_copy=x
            y_copy = y
            #вправо вверх
            while (x_copy <= 7) and (y_copy<=7) and (self.board[(x, y_copy)] == None):
                possible_moves.append((x_copy, y))
                x_copy +=1
                y_copy += 1
                

            x_copy=x
            y_copy = y
            #влево вверх
            while (x_copy<=0) and (y_copy <= 7) and (self.board[(x, y_copy)] == None):
                possible_moves.append((x_copy, y))
                x_copy-=1
                y_copy += 1

        return possible_moves

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


