from chessNav import *


class Piece:
    def __init__(
            self,  position: tuple, color: str, symbol=int, movesMade: int = 0
    ) -> None:
        self.board = chessNav()
        self.position = position
        self.movesMade = movesMade
        self.color = color
        self.character = chr(symbol)

        # def move(self, x1, y1, x2, y2):
        #     if (y1, x1) not in self.legal_moves:
        #         print('Illegal move!')
        #         return 0


class King(Piece):

    def __init__(self, color: str, position: tuple, symbol,  movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, movesMade)
        self.checked = False

    def move(self, x1, y1, x2, y2):
        if self.board.boardObj[y1][x1] != self:
            print(f'Na polu {x1, y1} nie ma K!')
            return
        if x2 not in [x1-1, x1, x1+1]:
            print("K can't go this high!")
            return
        if y2 not in [y1-1, y1, y1+1]:
            print("K can't go this wide!")
            return

        self.board.boardObj[y2][x2] = self.board.boardObj[y1][x1]


class Queen(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, movesMade)


class Bishop(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, movesMade)


class Knight(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, movesMade)


class Rook(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, movesMade)


class Pawn(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, movesMade)

    def move(self, x1, y1, x2, y2):
        if x1 != x2:
            print("Pawns don't cruise sideways!")
            return
        if y2 not in [y1 + 1, y1 - 1]:
            print("That, in basketball terms, is considered a travel")
            return

        self.board.boardObj[y2][x2] = self.board.boardObj[y1][x1]
