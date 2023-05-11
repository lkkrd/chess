class Piece:
    legal_moves = []
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

    def move(self, y1, x1, y2, x2):

        # stop jeśli dany obinekt nie jest zaimplemenowany
        if not hasattr(self, 'legal_moves'):
            print('Not implemented yet!')
            return

        # stop jeśli dany obiekt nie może się tam ruszyć
        if (y2, x2) not in self.legal_moves:
            print(f"I don't think {y2, x2} is a legal move...")
            return

        # stop jeśli miejsce jest zajęte
        if (self.board[y2][x2]) != ' ':
            print("You can't move there! Use 'take' method instead.")
            return

        # algorytm poruszania bierki
        self.board[y2][x2] = self.board[y1][x1]
        self.board[y1][x1] = ' '
        self.movesMade += 1
        self.position = (y2, x2)
        self.updateLegalMoves()


class King(Piece):

    def __init__(self, position: tuple, color: str, symbol, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)
        self.checked = False
        self.legal_moves = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                self.legal_moves.append((int(self.position[0]) + i, int(self.position[1] + j)))

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

    # zmiana pozycji pionka
    def updateLegalMoves(self):
        self.legal_moves = []
        if self.color == 'black':
            self.legal_moves.append((self.position[0] + 1, self.position[1]))

        if self.color == 'white':
            self.legal_moves.append((self.position[0] - 1, self.position[1]))
