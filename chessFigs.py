class Piece:
    def __init__(
            self,  position: tuple, color: str, symbol: int, board: list, movesMade: int = 0
    ) -> None:
        self.board = board
        self.position = position
        self.movesMade = movesMade
        self.color = color
        self.symbol = symbol
        self.legal_moves = []
        self.attack_moves = []
        self.updateLegalMoves()
        self.updateAttackMoves()

    def __str__(self):
        return chr(self.symbol)

    def move(self, y1, x1, y2, x2):

        # stop jeśli miejsce jest zajęte
        if (self.board[y2][x2]) != ' ':
            print("You can't move there! Use 'take' method instead.")
            return

        # stop jeśli dany obiekt nie może się tam ruszyć
        if (y2, x2) not in self.legal_moves:
            print(f"I don't think {y2, x2} is a legal move...")
            return

        # algorytm poruszania bierki
        self.board[y2][x2] = self.board[y1][x1]
        self.board[y1][x1] = ' '
        self.movesMade += 1
        self.position = (y2, x2)
        self.updateLegalMoves()
        self.updateAttackMoves()

    def take(self, y1, x1, y2, x2):

        # algorytm poruszania bierki
        self.board[y2][x2] = self.board[y1][x1]
        self.board[y1][x1] = ' '
        self.movesMade += 1
        self.position = (y2, x2)

    # jeśli nie zaimplementowane
    def updateLegalMoves(self):
        print('updateLegalMoves to be implemented')

    def updateAttackMoves(self):
        self.attack_moves = self.legal_moves
        for move in self.attack_moves:
            if self.board[move[0]][move[1]] != ' ':
                continue
            else:
                self.attack_moves.remove(move)


class King(Piece):

    def __init__(self, position: tuple, color: str, symbol, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)
        self.checked = False

    def updateLegalMoves(self):
        self.legal_moves = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                y = self.position[0] + i
                x = self.position[1] + j
                if not (x in range(1, 9) and y in range(1, 9)):
                    continue
                self.legal_moves.append((y, x))


class Queen(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)

    def updateLegalMoves(self):
        self.legal_moves = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                # case ruchu poziomego
                if i == 0 or j == 0:
                    for k in range(1, 8):
                        y = self.position[0] + i * k
                        x = self.position[1] + j * k

                        if not (x in range(1, 9) and y in range(1, 9)):
                            break
                        else:
                            self.legal_moves.append((y, x))
        # case ruchu po przekątnej
        for i in [-1, 1]:
            for j in [-1, 1]:
                for k in range(1, 8):
                    y = self.position[0] + i * k
                    x = self.position[1] + j * k

                    if not (x in range(1, 9) and y in range(1, 9)):
                        break
                    else:
                        self.legal_moves.append((y, x))


class Bishop(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)

    def updateLegalMoves(self):
        self.legal_moves = []
        for i in [-1, 1]:
            for j in [-1, 1]:
                for k in range(1, 8):
                    y = self.position[0] + i * k
                    x = self.position[1] + j * k

                    if not (x in range(1, 9) and y in range(1, 9)):
                        break
                    else:
                        self.legal_moves.append((y, x))


class Knight(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)

    def updateLegalMoves(self):
        self.legal_moves = []
        for i in [-2, -1, 1, 2]:
            for j in [-2, -1, 1, 2]:
                if abs(i) != abs(j):
                    y = self.position[0] + i
                    x = self.position[1] + j
                    if x in range(1, 9) and y in range(1, 9):
                        self.legal_moves.append((y, x))


class Rook(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)

    def updateLegalMoves(self):
        self.legal_moves = []
        for j in range(1, 8):
            # case ruchu w dół
            y = self.position[0] + j
            x = self.position[1]

            if (x in range(1, 9) and y in range(1, 9)):
                self.legal_moves.append((y, x))

            # case ruchu w górę
            y = self.position[0] - j
            x = self.position[1]

            if (x in range(1, 9) and y in range(1, 9)):
                self.legal_moves.append((y, x))

            # case ruchu w prawo
            y = self.position[0]
            x = self.position[1] + j

            if (x in range(1, 9) and y in range(1, 9)):
                self.legal_moves.append((y, x))

            # case ruchu w lewo
            y = self.position[0]
            x = self.position[1] - j

            if (x in range(1, 9) and y in range(1, 9)):  # warunek dodania
                self.legal_moves.append((y, x))

            # algorytm można przyspieszyć porzucając case po pierwszym niespełnionym warunku dodania


class Pawn(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)

    def updateLegalMoves(self):
        self.legal_moves = []
        height = self.position[0]
        width = self.position[1]
        if self.color == 'black':
            if height + 1 in range(1, 9):
                self.legal_moves.append((height + 1, width))
                if self.movesMade == 0:
                    self.legal_moves.append((height + 2, width))

        if self.color == 'white':
            if height - 1 in range(1, 9):
                self.legal_moves.append((height - 1, width))
                if self.movesMade == 0:
                    self.legal_moves.append((height - 2, width))

    def updateAttackMoves(self):
        self.attack_moves = []
        y = self.position[0]
        x = self.position[1]
        if self.color == 'white':
            self.attack_moves = [(y - 1, x - 1),
                                 (y - 1, x + 1)]
            for move in self.attack_moves:
                if move[0] in range(1, 9) and move[1] in range(1, 9):
                    if isinstance(self.board[move[0]][move[1]], Piece):
                        continue
                else:
                    self.attack_moves.remove(move)

        if self.color == 'black':
            self.attack_moves = [(y + 1, x - 1),
                                 (y + 1, x + 1)]
            for move in self.attack_moves:
                if move[0] in range(1, 9) and move[1] in range(1, 9):
                    if isinstance(self.board[move[0]][move[1]], Piece):
                        continue
                else:
                    self.attack_moves.remove(move)
