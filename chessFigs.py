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

class King(Piece):

    def __init__(self, position: tuple, color: str, symbol, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)
        self.checked = False
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                x = int(self.position[0]) + i
                y = int(self.position[1]) + j
                self.legal_moves.append((y, x))

class Queen(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)

        # ruchy w poziomie i pionie
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 or j == 0:
                    # poruszanie w poziomie lub pionie
                    for k in range(1, 8):
                        x = int(self.position[0]) + i * k
                        y = int(self.position[1]) + j * k
                        if x < 1 or x > 7 or y < 1 or y > 7:
                            # wyjście poza planszę
                            break
                        else:
                            # pole wolne
                            self.legal_moves.append((y, x))

        # ruchy po przekątnych
        for i in [-1, 1]:
            for j in [-1, 1]:
                for k in range(1, 8):
                    x = int(self.position[0]) + i * k
                    y = int(self.position[1]) + j * k
                    if x < 1 or x > 7 or y < 1 or y > 7:
                        # wyjście poza planszę
                        break
                    else:
                        # pole wolne
                        self.legal_moves.append((y, x))


class Bishop(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)

        for i in [-1, 1]:
            for j in [-1, 1]:
                for k in range(1, 8):
                    x = int(self.position[0]) + i * k
                    y = int(self.position[1]) + j * k
                    # wyjście poza planszę
                    if x < 1 or x > 7 or y < 1 or y > 7:
                        break
                    else:
                        self.legal_moves.append((y, x))


class Knight(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)

        #tworzenie tablicy legal_moves
        for i in [-2, -1, 1, 2]:
            for j in [-2, -1, 1, 2]:
                if abs(i) != abs(j):
                    x = int(self.position[0]) + i
                    y = int(self.position[1]) + j
                    if x in range(1, 9) and y in range(1, 9):
                        self.legal_moves.append((y, x))

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
        for i in [-1, 1]:
            for j in range(1, 8):
                x = int(self.position[0]) + i * j
                y = int(self.position[1])
                # wyjście poza planszę
                if x < 1 or x > 8:
                    break
                else:
                    # pole wolne
                    self.legal_moves.append((y, x))
            for j in range(1, 8):
                x = int(self.position[0])
                y = int(self.position[1]) + i * j
                # wyjście poza planszę
                if y < 1 or y > 8:
                    break
                else:
                    # pole wolne
                    self.legal_moves.append((y, x))

class Pawn(Piece):
    def __init__(self, position: tuple, color: str, symbol: int, board: list, movesMade: int = 0) -> None:
        super().__init__(position, color, symbol, board, movesMade)

        #tworzenie legal_moves
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

        #tworzenie attack_moves
        if color == 'white':
            self.attack_moves = [(position[0] - 1, position[1] - 1), (position[0] - 1, position[1] + 1)]
            for move in self.attack_moves:
                if self.board[move[0]][move[1]] != ' ':
                    continue
                else:
                    self.attack_moves.remove(move)

    def updateLegalMoves(self):
        self.legal_moves = []
        if self.color == 'black':
            if (self.position[0] + 1, self.position[1]) in range(0, 9):
                self.legal_moves.append((self.position[0] + 1, self.position[1]))

        if self.color == 'white':
            if (self.position[0] - 1, self.position[1]) in range(0, 9):
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
            self.attack_moves = [(self.position[0] - 1, self.position[1] - 1), (self.position[0] - 1, self.position[1] + 1)]
            for move in self.attack_moves:
                if self.board[move[0]][move[1]] != ' ':
                    continue
                else:
                    self.attack_moves.remove(move)

        if self.color == 'black':
            for move in self.attack_moves:
                if self.board[move[0]][move[1]] != ' ':
                    continue
                else:
                    self.attack_moves.remove(move)