from board import board
from typing import Tuple
from typing import Dict, List, Tuple

FigureDict = Dict[str, Dict[str, List[Tuple[int, int]]]]

class InvalidMoveError(Exception):
    pass

class InvalidFigureCall(Exception):
    pass

class NoneFigureError(Exception):
    pass

class game():
    def __init__(self) -> None:
        self.board=board()
        self.history_boards=[self.board]
        self.history_moves=[]
    
    def make_board_from_figures_dict(figures_dict):
        
    def is_game_over(self):
        # true если для одной из сторон любой ход ведет в шах
        # если true выдает кто выиграл
        # если игра продолжается выдает false None
        # провер
        return False,None

    def is_check(self,color):
        # true если король цвета color находится под шахом
        # т.е. если бы сторона opposite_color ходила дважды то они бы могли его срубить т.е.
        # одна из фигур могла бы оказаться на месте короля 
        king_position=self.board.figures_dict[color]["K"]
        if color=="white":
            if king_position in self.board.all_possible_moves_for_color("black"):    
                return True
            else:
                return False
        if color=="black":
            if king_position in self.board.all_possible_moves_for_color("white"):    
                return True
            else:
                return False

        
      
    def move(self,move,creative=False):
        
        if move=="0-0":
            pass
        elif move=="0-0-0":
            pass
        elif "=" in move:
            pass
        fig,old_hor,old_ver,new_hor,new_ver=move[0],move[1],int(move[2]),move[3],int(move[4])
        decode={i[0]:i[1] for i in list(zip(list("abcdefgh"),[i for i in range(8)]))}
        
        old_hor_decode=decode[old_hor]
        new_hor_decode=decode[new_hor]
        old_ver_decode=old_ver-1
        new_ver_decode=new_ver-1

        if self.board.board[(old_ver_decode,old_hor_decode)]==None:
            raise NoneFigureError(f"there are no figure on {old_hor}{old_ver} ")

        if fig!=self.board.board[(old_ver_decode,old_hor_decode)].name:
            print(fig)
            print(self.board[(old_ver_decode,old_hor_decode)].name)
            print(old_hor_decode,old_ver_decode)
            raise InvalidFigureCall(f"on {old_hor}{old_ver} not a {fig}")
            
        if (new_ver_decode,new_hor_decode) not in self.board.possible_moves((old_ver_decode,old_hor_decode)):
            raise InvalidMoveError(f"fig on {old_hor}{old_ver} cant go on a {new_hor}{new_ver}")
        


        old_fig=self.board.board[(old_ver_decode,old_hor_decode)]
        color=old_fig.color
        name=old_fig.name
        self.board.board[(new_ver_decode,new_hor_decode)]=old_fig
        self.board.board[(old_ver_decode,old_hor_decode)]=None
    
        self.board.figures_dict[color][name].remove([old_ver_decode,old_hor_decode])
        self.board.figures_dict[color][name].append([new_ver_decode,new_hor_decode])

        self.history_boards.append(self.board)    
        self.history_moves.append(move)
        

    def start(self):
        i=0
        print(g.board)
        gg=False
        while not (gg):
            if i%2==0:
                print("white for move")
            if i%2==1:
                print("black for move")
            move=input()
            if input!="gg":
                self.move(move)
            else:
                gg=True
            print(g.board)
            i+=1
            


g=game()

g.move("Pe2e4")
g.move("Pg2g4")
g.move("Pf2f4")
g.move("Bf1f5",creative=True)
g.move("Ke2b4",creative=True)


print(g.board)
print(g.board.board[(0,5)].name)


print(g.board.possible_moves((0,4)))
print(g.board.possible_moves((0,5)))
print(g.board.possible_moves((0,6)))
