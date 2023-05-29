from chessFigs import *
# from chessNav import *

# towrzenie szachownicy z figurami
figure_codes = []
start = 9812
for i in range(12):
    figure_codes.append(start + i)

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

board = [
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

# zamiana wszystkich pionków na obiekty
for row in board:
    for piece in row:
        if piece == bP:
            # Dlaczego to nie działa?
            # currField = board[board.index(row)][row.index(piece)]
            # currField = Pawn((row.index(piece), 2), 'black', bP, board)
            board[board.index(row)][row.index(piece)] = Pawn(
                (2, row.index(piece)), 'black', bP, board)
        if piece == wP:
            board[board.index(row)][row.index(piece)] = Pawn(
                (7, row.index(piece)), 'white', wP, board)
        if piece == bR:
            board[board.index(row)][row.index(piece)] = Rook(
                (1, row.index(piece)), 'black', bR, board)
        if piece == wR:
            board[board.index(row)][row.index(piece)] = Rook(
                (8, row.index(piece)), 'white', wR, board)
        if piece == bN:
            board[board.index(row)][row.index(piece)] = Knight(
                (1, row.index(piece)), 'black', bN, board)
        if piece == wN:
            board[board.index(row)][row.index(piece)] = Knight(
                (8, row.index(piece)), 'white', wN, board)
        if piece == bB:
            board[board.index(row)][row.index(piece)] = Bishop(
                (1, row.index(piece)), 'black', bB, board)
        if piece == wB:
            board[board.index(row)][row.index(piece)] = Bishop(
                (8, row.index(piece)), 'white', wB, board)
        if piece == bQ:
            board[board.index(row)][row.index(piece)] = Queen(
                (1, row.index(piece)), 'black', bQ, board)
        if piece == wQ:
            board[board.index(row)][row.index(piece)] = Queen(
                (8, row.index(piece)), 'white', wQ, board)
        if piece == bK:
            board[board.index(row)][row.index(piece)] = King(
                (1, row.index(piece)), 'black', bK, board)
        if piece == wK:
            board[board.index(row)][row.index(piece)] = King(
                (8, row.index(piece)), 'white', wK, board)

# zamiana self.position z (x, y) na (y, x)
# for row in board:
#     for piece in row:
#         if isinstance(piece, Piece):
#             holder = piece.position
#             piece.position = holder[1], holder[0]


def printBoard():
    for row in board:
        print('')
        for piece in row:
            print(piece, end=' ')
    print()


def resetBoard():
    global board
    board = [
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


def move(y1, x1, y2, x2):
    if board[y1][x1] == ' ':
        print("that's a blank field!")
        return
    currFig = board[y1][x1]
    currFig.move(y1, x1, y2, x2)
    printBoard()


def take(y1, x1, y2, x2):
    currFig = getFigure(y1, x1)
    currFig.updateAttackMoves()
    if (y2, x2) not in currFig.attack_moves:
        print(f'{y2, x2} is not a field to take.')
        return
    currFig.take(y1, x1, y2, x2)
    printBoard()


def getFigure(y1, x1):
    if board[y1][x1] == ' ':
        return 'Blank field'
    return board[y1][x1]


printBoard()

# Dlaczego obiekty nie wyświetlają się swoją postacią __str__?
# for i in range(1, 9):
#     for j in [1, 2, 7, 8]:
#         print(f'{getFigure(j, i)} position: {getFigure(j, i).position}')
