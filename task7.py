class Chessboard:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 17)

    def is_valid_move(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def place_piece(self, x, y, piece):
        if self.is_valid_move(x, y):
            self.board[x][y] = piece
        else:
            raise IndexError("Invalid position!")


class Piece:
    def __init__(self, chessboard: Chessboard, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.type = None
        self.chessboard = chessboard

    def move(self, new_x, new_y):
        raise NotImplementedError("Subclasses must implement this method")


class King(Piece):
    def __init__(self, chessboard: Chessboard, x, y, color):
        super().__init__(chessboard, x, y, color)
        self.type = 'K'
        self.chessboard.place_piece(self.x, self.y, self.type)

    def move(self, new_x, new_y):
        if abs(new_x - self.x) <= 1 and abs(new_y - self.y) <= 1:
            self.chessboard.place_piece(self.x, self.y, '')
            self.chessboard.place_piece(new_x, new_y, self.type)
        else:
            raise IndexError("Invalid move for King!")


class Rook(Piece):
    def __init__(self, chessboard: Chessboard, x, y, color):
        super().__init__(chessboard, x, y, color)
        self.type = 'R'
        self.chessboard.place_piece(self.x, self.y, self.type)

    def move(self, new_x, new_y):
        if (new_x == self.x and new_y != self.y) or (new_x != self.x and new_y == self.y):
            self.chessboard.place_piece(self.x, self.y, '')
            self.chessboard.place_piece(new_x, new_y, self.type)
        else:
            raise IndexError("Invalid move for Rook!")


class Knight(Piece):
    def __init__(self, chessboard: Chessboard, x, y, color):
        super().__init__(chessboard, x, y, color)
        self.type = 'N'
        self.chessboard.place_piece(self.x, self.y, self.type)

    def move(self, new_x, new_y):
        if (abs(new_x - self.x) == 2 and abs(new_y - self.y) == 1) or \
           (abs(new_x - self.x) == 1 and abs(new_y - self.y) == 2):
            self.chessboard.place_piece(self.x, self.y, '')
            self.chessboard.place_piece(new_x, new_y, self.type)
        else:
            raise IndexError("Invalid move for Knight!")

class Queen(Piece):
    def __init__(self, chessboard: Chessboard, x, y, color):
        super().__init__(chessboard, x, y, color)
        self.type = 'Q'
        self.chessboard.place_piece(self.x, self.y, self.type)

    def move(self, new_x, new_y):
        if new_x == self.x or new_y == self.y or abs(new_x - self.x) == abs(new_y - self.y):
            self.chessboard.place_piece(self.x, self.y, '')
            self.chessboard.place_piece(new_x, new_y, self.type)
        else:
            raise IndexError("Invalid move for Queen!")


if __name__ == '__main__':
    chessboard = Chessboard()
    king = King(chessboard, 0, 0, 'W')
    rook = Rook(chessboard,1, 1, 'B')
    knight = Knight(chessboard,2, 2, 'W')
    queen = Queen(chessboard,3, 3, 'B')

    chessboard.print_board()

    rook.move(1, 4)
    king.move(1, 1)
    knight.move(4, 3)
    queen.move(4, 4)

    chessboard.print_board()
