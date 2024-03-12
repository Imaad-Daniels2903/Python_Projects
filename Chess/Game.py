from Board import make_board, make_pieces

board = make_board()
make_pieces(board)
for disp in range(len(board)):
    print(board[disp])