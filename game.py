from board import board
from typing import Tuple


class game():
    def __init__(self) -> None:
        self.board=board()
        self.history=[self.board]

    def game_over(self):# true если для одной из сторон любой ход ведет в шах
        pass

    def is_check(self,color):
        # true если король цвета color находится под шахом
        # т.е. если бы сторона opposite_color ходила дважды то они бы могли его срубить т.е.
        # одна из фигур могла бы оказаться на месте короля 
        self.__king_position=self.board.figures_dict[color]["K"]

        
        pass

    




    def move(self):
        
        pass

    def start(self):
        while not (self.game_over()):
            pass
    
g=game()

print(g.get_all_moves((0,4)))

