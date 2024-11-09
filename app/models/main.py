from app.models.entities import(
    BLACK_BISHOP,
    BLACK_HORSE,
    BLACK_KING,
    BLACK_PAWN,
    BLACK_QUEEN,
    BLACK_ROOK,
    WHITE_BISHOP,
    WHITE_CELL,
    GREEN_CELL,
    WHITE_HORSE,
    WHITE_KING,
    WHITE_PAWN,
    WHITE_QUEEN,
    WHITE_ROOK,
)


def create_board()-> list[int]:
    """
    Cria o tabuleiro
    """
    board = []

    for line in range(8):
        row = []
        for column in range(8):
            
            if line % 2 == 0:
                if column % 2 == 0:
                    row.append(WHITE_CELL) # POSICIONANDO AS CELULAS BRANCAS
                else:
                    row.append(GREEN_CELL) # POSICIONANDO AS CELULAS VERDES
            else:
                if column % 2 == 0: 
                    row.append(GREEN_CELL) # POSICIONANDO AS CELULAS BRANCAS
                else:
                    row.append(WHITE_CELL) # POSICIONANDO AS CELULAS VERDES

        board.append(row)

    return board


def place_pieces(board):
    """
    Posiciona as peças no tabuleiro
    """

    # PRETAS
    board[0][0] = BLACK_ROOK
    board[0][1] = BLACK_HORSE
    board[0][2] = BLACK_BISHOP
    board[0][3] = BLACK_QUEEN
    board[0][4] = BLACK_KING
    board[0][5] = BLACK_BISHOP
    board[0][6] = BLACK_HORSE
    board[0][7] = BLACK_ROOK
    board[1][0] = BLACK_PAWN
    board[1][1] = BLACK_PAWN
    board[1][2] = BLACK_PAWN
    board[1][3] = BLACK_PAWN
    board[1][4] = BLACK_PAWN
    board[1][5] = BLACK_PAWN
    board[1][6] = BLACK_PAWN
    board[1][7] = BLACK_PAWN

    # BRANCAS
    board[7][0] = WHITE_ROOK
    board[7][1] = WHITE_HORSE
    board[7][2] = WHITE_BISHOP
    board[7][3] = WHITE_QUEEN
    board[7][4] = WHITE_KING
    board[7][5] = WHITE_BISHOP
    board[7][6] = WHITE_HORSE
    board[7][7] = WHITE_ROOK
    board[6][0] = WHITE_PAWN
    board[6][1] = WHITE_PAWN
    board[6][2] = WHITE_PAWN
    board[6][3] = WHITE_PAWN
    board[6][4] = WHITE_PAWN
    board[6][5] = WHITE_PAWN
    board[6][6] = WHITE_PAWN
    board[6][7] = WHITE_PAWN


def show_board(board):
    for row in board:
        print(row)


board = create_board()

place_pieces(board)
