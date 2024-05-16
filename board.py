from itertools import product
from figure import figure
from typing import Tuple ,Dict,List

FigureToPlace = Dict[str, Dict[str, List[Tuple[int, int]]]]

class board():
    def __init__(self) -> None:

        self.figures_dict={ # фигура- к клетке
            # точнее фигура к нескольким клеткам т.к. есть одинаковые фигуры на доске
            # создан что бы при подсчете шаха не перебирать все клетки доски
            # а только фигуры, более того только фигуры определенного цвета
            "white":{
                "P":[(1,i) for i in range(8)],
                "R":[(0,0),(0,7)],
                "N":[(0,1),(0,6)],
                "B":[(0,2),(0,5)],
                "Q":[(0,3)],
                "K":[(0,4)]
            },
            "black":{
                "P":[(6,i) for i in range(8)],
                "R":[(7,0),(7,7)],
                "N":[(7,1),(7,6)],
                "B":[(7,2),(7,5)],
                "Q":[(7,3)],
                "K":[(7,4)]
            }
        }
        self.make_board_from_figures_dict(figures_dict=self.figures_dict)


    def make_board_from_figures_dict(self,figures_dict:FigureToPlace,need_empty_board_first=True,board_size=(8,8)):
        self.board=self.make_empty_board()
       
        for color,pieces in figures_dict.items():    
            for piece in pieces.keys():
                for place in pieces[piece]:
                    self.board[place]=figure(self,color,piece,place)

    def make_empty_board(self,board_size=(8,8),rectangle=True):
        if rectangle:
            self.board={tuple(i): None for i in # клетка - к фигуре
                    list(product([i for i in range(board_size[0])], [i for i in range(board_size[1])]))}
        return self.board

    def all_possible_moves_for_color(self,color):
        if color=="white":
            #ищем все ходы черных фигур
            #для этого сначала получаем все позиции черных после запускаме all_possible_moves от каждой из них
            all_pieces=[]
            for piece_type, positions in self.board.figures_dict["black"].items():
                all_pieces.extend(positions)
            
            all_possible_moves=[]
            for piece in all_pieces:
                all_possible_moves.extend(self.board.possible_moves(piece))
        
        if color=="black":
            all_pieces=[]
            for piece_type, positions in self.board.figures_dict["white"].items():
                all_pieces.extend(positions)
            
            all_possible_moves=[]
            for piece in all_pieces:
                all_possible_moves.extend(self.board.possible_moves(piece))
        
        return all_possible_moves

    def possible_moves(self, coordinates: Tuple):
        name = self.board[coordinates].name
        y = coordinates[0]
        x = coordinates[1]

        possible_moves = []
        
        if name == "P":
            if self.board[coordinates].color=="white":
                # тут может быть еще на самом деле en-passant но мне похрен его реализовывать
                # превращение пешки тоже будет реализовывать другой скрипт
                if y==1 and self.board[(2,x)]==None and self.board[(3,x)]==None:
                    possible_moves=[(2,x),(3,x)]
                elif self.board[(y+1,x)]!=None: 
                    possible_moves=[(y+1,x)]
            else:
                if y==6 and self.board[(5,x)]==None and self.board[(4,x)]==None:
                    possible_moves=[(5,x),(4,x)]
                elif self.board[(y-1,x)]!=None: 
                    possible_moves=[(y-1,x)]


        if name == "K":
            possible_moves = [(y - 1, x - 1), (y - 1, x), (y - 1, x + 1), (y, x - 1), (y, x + 1), (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)]
            ans=[]
            flag=True
            for i in possible_moves:
                for j in i:
                    if j<=0 or j>7:
                        flag=False

                if flag:
                    if self.board[(i[0],i[1])]==None:
                        ans.append(i)
                flag=True
            
            possible_moves=ans

        if name == "N":
            possible_moves = [(y - 2, x + 1), (y - 1, x + 2), (y + 1, x + 2), (y + 2, x + 1), (y + 2, x - 1), (y + 1, x - 2), (y - 1, x - 2), (y - 2, x - 1)]
            ans=[]
            flag=True
            for i in possible_moves:
                for j in i:
                    if j<=0 or j>7:
                        flag=False

                if flag:
                    if self.board[(i[0],i[1])]==None:
                        ans.append(i)
                flag=True
            
            possible_moves=ans

        if name == "R" or name=="Q":
            
            y_copy = y

            # двигаемся влево пока на наших полях None и пока мы не вышли за пределы доски
            while (y_copy >= 0) and ((y_copy==y and x_copy==x) or self.board[(y_copy, x)] == None):
                y_copy -= 1
                possible_moves.append((y_copy, x))
                

            # вправо
            y_copy = y
            while (y_copy <= 7) and ((y_copy==y and x_copy==x) or self.board[(y_copy, x)] == None):
                y_copy += 1
                possible_moves.append((y_copy, x))
            

            # вверх
            x_copy = x
            while (x_copy <= 7) and ((y_copy==y and x_copy==x) or self.board[(y, x_copy)] == None):
                x_copy += 1
                possible_moves.append((y_copy, x))
              

            # вниз
            x_copy = x
            while (x_copy >= 0) and ((y_copy==y and x_copy==x) or self.board[(y, x_copy)] == None):
                x_copy -= 1
                possible_moves.append((y_copy, x))
                


        if name == "B" or name=="Q":
            
            y_copy = y
            x_copy = x

            # влево вниз
            while (y_copy >= 0) and (x_copy >= 0) and ((y_copy==y and x_copy==x) or self.board[(y_copy, x_copy)] == None):
                if not(y_copy==y and x_copy==x):
                    possible_moves.append((y_copy, x_copy))
                y_copy -= 1
                x_copy -= 1
                
                

            y_copy = y
            x_copy = x

            # влево вверх
            while (y_copy <= 7) and (x_copy >=0 ) and ((y_copy==y and x_copy==x) or self.board[(y_copy, x_copy)] == None):
                if not(y_copy==y and x_copy==x):
                    possible_moves.append((y_copy, x_copy))
                y_copy += 1
                x_copy -=1
                
            y_copy=y
            x_copy = x
            #вправо вверх
            while (y_copy <= 7) and (x_copy <= 7) and ((y_copy==y and x_copy==x) or self.board[(y_copy, x_copy)] == None):
                if not(y_copy==y and x_copy==x):
                    possible_moves.append((y_copy, x_copy))
                y_copy +=1
                x_copy += 1

                

            y_copy=y
            x_copy = x
            #вправо вниз
            while (y_copy>=0) and (x_copy <= 7) and ((y_copy==y and x_copy==x) or self.board[(y_copy, x_copy)] == None):
                if not(y_copy==y and x_copy==x):
                    possible_moves.append((y_copy, x_copy))
                y_copy-=1
                x_copy += 1
                

        return possible_moves



    def __repr__(self) -> str:
        s=""
        for i in range(7,-1,-1):
            s+=str(i+1)+" "
            for j in range(8):
                if self.board[(i,j)]==None:
                    s+="--"+" "
                elif self.board[(i,j)].color=="white":
                    s+=f"w{self.board[(i,j)].name}"+" "
                elif self.board[(i,j)].color=="black":
                    s+=f"b{self.board[(i,j)].name}"+" "
            s+="\n"
        s=s+"  a  b  c  d  e  f  g  h"
        return s
    


if __name__=="__main__":
    b=board()

    print(b)


