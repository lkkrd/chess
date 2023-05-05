class chessNav:
    def __init__(self):

        figure_codes = []
        start = 9812
        for i in range(12):
            figure_codes.append(chr(start + i))

        bK = figure_codes[0]
        bQ = figure_codes[1]
        bR = figure_codes[2]
        bB = figure_codes[3]
        bN = figure_codes[4]
        bP = figure_codes[5]
        wK = figure_codes[6]
        wQ = figure_codes[7]
        wR = figure_codes[8]
        wB = figure_codes[9]
        wN = figure_codes[10]
        wP = figure_codes[11]

        self.board = [
            [' ', '1', '2', '3', '4', '5', '6', '7', '8'],
            ['1', bR, bN, bB, bQ, bK, bB, bN, bR],
            ['2', bP, bP, bP, bP, bP, bP, bP, bP],
            ['3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['7', wP, wP, wP, wP, wP, wP, wP, wP],
            ['8', wR, wN, wB, wQ, wK, wB, wN, wR],
        ]

    def printBoard(self):
        for row in self.board:
            print(row)

    def move(self, x1, y1, x2, y2):
        currFig = self.board[y1][x1]
        self.board[y2][x2] = currFig
        self.board[y1][x1] = ' '
        print(f'Move made: {currFig} to {x2, y2}.')
        self.printBoard()
