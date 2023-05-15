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

    def take(self, y1, x1, y2, x2):

        # algorytm poruszania bierki
        self.board[y2][x2] = self.board[y1][x1]
        self.board[y1][x1] = ' '
        self.movesMade += 1
        self.position = (y2, x2)
        self.updateLegalMoves()

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
        self.updateLegalMoves()
        self.updateAttackMoves()

    def updateLegalMoves(self):
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                x = int(self.position[0]) + i
                y = int(self.position[1]) + j
                if not (x in range(1, 9) and y in range(1, 9)):
                    continue
                self.legal_moves.append((y, x))

class Queen(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)
        self.updateLegalMoves()
    def updateLegalMoves(self):
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                #case ruchu poziomego
                if i == 0 or j == 0:
                    for k in range(1, 8):
                        x = int(self.position[0]) + i * k
                        y = int(self.position[1]) + j * k

                        if not (x in range(1, 9) and y in range(1, 9)):
                            break
                        else:
                            self.legal_moves.append((y, x))

        #case ruchu diagonalnego
        for i in [-1, 1]:
            for j in [-1, 1]:
                for k in range(1, 8):
                    x = int(self.position[0]) + i * k
                    y = int(self.position[1]) + j * k

                    if not (x in range(1, 9) and y in range(1, 9)):
                        break
                    else:
                        self.legal_moves.append((y, x))


class Bishop(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)
        self.updateLegalMoves()

    def updateLegalMoves(self):
        for i in [-1, 1]:
            for j in [-1, 1]:
                for k in range(1, 8):
                    x = int(self.position[0]) + i * k
                    y = int(self.position[1]) + j * k

                    if not (x in range(1, 9) and y in range(1, 9)):
                        break
                    else:
                        self.legal_moves.append((y, x))


class Knight(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)
        self.updateLegalMoves()

    def updateLegalMoves(self):
        self.legal_moves = []
        for i in [-2, -1, 1, 2]:
            for j in [-2, -1, 1, 2]:
                if abs(i) != abs(j):
                    x = int(self.position[0]) + i
                    y = int(self.position[1]) + j
                    if x in range(1, 9) and y in range(1, 9):
                        self.legal_moves.append((y, x))


class Rook(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)
        self.updateLegalMoves()
    def updateLegalMoves(self):
        for i in [-1, 1]:
            for j in range(1, 8):
                x = int(self.position[0]) + i * j
                y = int(self.position[1])

                if not (x in range(1, 9) and y in range(1, 9)):
                    break
                else:
                    self.legal_moves.append((y, x))

            for j in range(1, 8):
                x = int(self.position[0])
                y = int(self.position[1]) + i * j

                if not (x in range(1, 9) and y in range(1, 9)):
                    break
                else:
                    self.legal_moves.append((y, x))

class Pawn(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)
        self.updateLegalMoves()
        self.updateAttackMoves()

    def updateLegalMoves(self):
        self.legal_moves = []
        if self.color == 'black':
            if self.position[0] + 1 in range (1, 9) and self.position[1] in range(1, 9):
                self.legal_moves.append((self.position[0] + 1, self.position[1]))

        if self.color == 'white':
            if self.position[0] - 1 in range (1, 9) and self.position[1] in range(1, 9):
                self.legal_moves.append((self.position[0] - 1, self.position[1]))

    def updateAttackMoves(self):

        #przypadki skrajnego rzędu
        if self.position[0] == 8 and self.color == 'black':
            self.attack_moves = []
            return
        if self.position[0] == 1 and self.color == 'white':
            self.attack_moves = []
            return

        if self.color == 'white':
            self.attack_moves = [(self.position[0] - 1, self.position[1] - 1),
                                 (self.position[0] - 1, self.position[1] + 1)]
            for move in self.attack_moves:
                if self.board[move[0]][move[1]] != ' ':
                    continue
                else:
                    self.attack_moves.remove(move)

        if self.color == 'black':
            self.attack_moves = [(self.position[0] + 1, self.position[1] - 1),
                                 (self.position[0] + 1, self.position[1] + 1)]
            for move in self.attack_moves:
                if self.board[move[0]][move[1]] != ' ':
                    continue
                else:
                    self.attack_moves.remove(move)