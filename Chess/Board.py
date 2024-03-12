def make_board():
    colour = ''
    square = ''
    board = []
    bd = 0
    row = ''

    for bd in range(1, 9):
        blank = []
        for row in range(ord('a'), ord('h') + 1):
            if bd % 2 == 0:
                if (row % 2) == 0:
                    colour = 'B'
                else:
                    colour = 'W'
            else:
                if (row % 2) == 0:
                    colour = 'W'
                else:
                    colour = 'B'

            blank.append([chr(row) + str(bd)])
            blank[row - 97].append(colour)
        board.append(blank)
    return board


def make_pieces(board):
    for pawns in range(0, 8):
        board[1][pawns].append('WP')
        board[6][pawns].append('BP')
        if pawns == 0 or pawns == 7:
            board[0][pawns].append('WR')
            board[7][pawns].append('BR')
        elif pawns == 1 or pawns == 6:
            board[0][pawns].append('WN')
            board[7][pawns].append('BN')
        elif pawns == 2 or pawns == 5:
            board[0][pawns].append('WB')
            board[7][pawns].append('BB')
        elif pawns == 3:
            board[0][pawns].append('WQ')
            board[7][pawns].append('BQ')
        elif pawns == 4:
            board[0][pawns].append('WK')
            board[7][pawns].append('BK')
