class figure():
    def __init__(self,board,color,name,place) -> None:
        self.board=board # на какой доске стоит фигура
        self.color=color 
        self.name=name # какая мы фигура (пешка ,конь, etc)
        self.place=place # где мы стоим
    
    def move(self,new_place): 
        # этот метод будет вызывать доска class board который 
        #в свою очередь будет вызывать игра class game
        # game будет обрабатывать ход и переводить его из человеческой нотации
        # в компьютерную 
        # board будет 
        # 1) направлять какая фигура будет ходить и вызывать у нее свой метод move
        # 2) следить за extra ходами 
       
        #1) мы перешли на пустую клетку
        self.board.board[new_place]=self
        self.board.board[self.place]=None
        self.place=new_place
        
        
        # extra 
        # мы пешка и мы перешли на последнюю вертикаль и должны превратиться
        # (горизонталь , в кого превращаемся)
        # произошла рокировка 
        # короткая рокировка будет (-1,color)
        # длинная рокировка будет (-2,color)  
        # произошло взятие на проходе 
        # if self.color=white надо удалить нижнюю пешку

        
