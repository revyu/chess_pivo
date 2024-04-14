from board import board
from typing import Tuple


class game():
    def __init__(self) -> None:
        self.board=board()
        self.history_boards=[self.board]
        self.history_moves=[]

    def game_over(self):# true если для одной из сторон любой ход ведет в шах
        if len(self.history_moves)==3:# чисто для проверки пока что
            return True
        else:
            return False

    def is_check(self,color):
        # true если король цвета color находится под шахом
        # т.е. если бы сторона opposite_color ходила дважды то они бы могли его срубить т.е.
        # одна из фигур могла бы оказаться на месте короля 
        self.__king_position=self.board.figures_dict[color]["K"]

        
        pass

    def move(self,move):
        
        if move=="0-0":
            pass
        elif move=="0-0-0":
            pass
        elif "=" in move:
            pass
        fig,old_hor,old_ver,new_hor,new_ver=move[0],move[1],int(move[2]),move[3],int(move[4])
        decode={i[0]:i[1] for i in list(zip(list("abcdefgh"[::-1]),[i for i in range(7)]))}

        old_hor_decode=decode[old_hor]
        new_hor_decode=decode[new_hor]
        old_ver_decode=old_ver-1
        new_ver_decode=new_ver-1

        if self.board.board[(old_ver_decode,old_hor_decode)]==None:
            raise KeyError(f"there are no figure on {old_hor}{old_ver} ")

        if fig!=self.board.board[(old_ver_decode,old_hor_decode)].name:
            print(fig)
            print(self.board[(old_ver_decode,old_hor_decode)].name)
            print(old_hor_decode,old_ver_decode)
            raise KeyError(f"on {old_hor}{old_ver} not a {fig}")
            

        self.board.board[(old_ver_decode,old_hor_decode)].move((new_ver_decode,new_hor_decode))



        self.history_boards.append(self.board)    
        self.history_moves.append(move)

    def start(self):
        i=0
        print(g.board)
        while not (self.game_over()):
            if i%2==0:
                print("white for move")
            if i%2==1:
                print("black for move")
            
            self.move(input())
            print(g.board)
            i+=1
            


g=game()

g.start()

#print(g.board.get_all_moves((6,6)))

