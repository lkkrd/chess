class Piece:
    def __init__(
            self,  position: tuple, color: str, symbol: int, board: list, movesMade: int = 0
    ) -> None:
        self.board = board
        self.position = position
        self.movesMade = movesMade
        self.color = color
        self.symbol = symbol

    def __str__(self):
        return chr(self.symbol)

        # def move(self, x1, y1, x2, y2):
        #     if (y1, x1) not in self.legal_moves:
        #         print('Illegal move!')
        #         return 0

    def move(self, x1, y1, x2, y2):
        # czy na danym polu jest pionek
        if not isinstance(self.board[y1][x1], Pawn):
            print(f'Field {x1, y1} is not a pawn!')
            return
        # czy pionek może ruszyć się na wskazane pole
        if (y2, x2) not in self.legal_moves:
            print(f"I don't think {x2, y2} is a legal move...")
            return
        # algorytm poruszania pionka
        self.board[y2][x2] = self.board[y1][x1]
        self.board[y1][x1] = ' '
        self.movesMade += 1
        self.position = (y2, x2)
        self.updateLegalMoves()


class King(Piece):

    def __init__(self, color: str, position: tuple, symbol, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)
        self.checked = False

    # def move(self, x1, y1, x2, y2):
    #     if self.board.boardObj[y1][x1] != self:
    #         print(f'Na polu {x1, y1} nie ma K!')
    #         return
    #     if x2 not in [x1-1, x1, x1+1]:
    #         print("K can't go this high!")
    #         return
    #     if y2 not in [y1-1, y1, y1+1]:
    #         print("K can't go this wide!")
    #         return

        # self.board.boardObj[y2][x2] = self.board.boardObj[y1][x1]


class Queen(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)


class Bishop(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)


class Knight(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)


class Rook(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)


class Pawn(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)
        self.legal_moves = []
        if self.color == 'black':
            self.legal_moves.append((self.position[1] + 1, self.position[0]))
            if movesMade == 0:
                self.legal_moves.append(
                    (self.position[1] + 2, self.position[0]))

        if self.color == 'white':
            self.legal_moves.append((self.position[1] - 1, self.position[0]))
            if movesMade == 0:
                self.legal_moves.append(
                    (self.position[1] - 2, self.position[0]))

        # self.attack_moves = []

    def updateLegalMoves(self):
        if self.color == 'black':
            self.legal_moves = (self.position[1] + 1, self.position[0])

        if self.color == 'white':
            self.legal_moves = (self.position[1] - 1, self.position[0])

    # def move(self, x1, y1, x2, y2):
    #     if x1 != x2:
    #         print("Pawns don't cruise sideways!")
    #         return
    #     if y2 not in [y1 + 1, y1 - 1]:
    #         print("That, in basketball terms, is considered a travel")
    #         return

    #     self.board.boardObj[y2][x2] = self.board.boardObj[y1][x1]
