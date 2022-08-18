from math import fabs

chess_board = [[['R', 'w'], ['p', 'w'], None, None, None, None, ['p', 'b'], ['R', 'b']],
               [['N', 'w'], ['p', 'w'], None, None, None, None, ['p', 'b'], ['N', 'b']],
               [['B', 'w'], ['p', 'w'], None, None, None, None, ['p', 'b'], ['B', 'b']],
               [['Q', 'w'], ['p', 'w'], None, None, None, None, ['p', 'b'], ['Q', 'b']],
               [['K', 'w'], ['p', 'w'], None, None, None, None, ['p', 'b'], ['K', 'b']],
               [['B', 'w'], ['p', 'w'], None, None, None, None, ['p', 'b'], ['B', 'b']],
               [['N', 'w'], ['p', 'w'], None, None, None, None, ['p', 'b'], ['N', 'b']],
               [['R', 'w'], ['p', 'w'], None, None, None, None, ['p', 'b'], ['R', 'b']]]

chess_board_positions = []
for i in range(8):
    for j in range(8):
        chess_board_positions += [[i, j]]


class ValidMoves(object):
    def __init__(self, pos):
        self.pos = pos
        self.piece_type = chess_board[pos[0]][pos[1]][0]
        self.side = chess_board[pos[0]][pos[1]][1]

    def get_moves(self):
        if self.piece_type == 'R':
            return self.rook_moves(self.pos, self.side)
        elif self.piece_type == 'B':
            return self.bishop_moves(self.pos, self.side)
        elif self.piece_type == 'N':
            return self.knight_moves(self.pos, self.side)
        elif self.piece_type == 'Q':
            return self.queen_moves(self.pos, self.side)
        elif self.piece_type == 'K':
            return self.king_moves(self.pos, self.side)
        elif self.piece_type == 'p':
            return self.pawn_moves(self.pos, self.side)

    @staticmethod
    def rook_moves(pos, side):
        possible_moves = []

        for m in range(1, 8 - pos[0]):
            if not chess_board[pos[0] + m][pos[1]]:
                possible_moves += [[pos[0] + m, pos[1]]]
            elif (m == 1 and chess_board[pos[0] + m][pos[1]][1] != side) or \
                    (chess_board[pos[0] + m][pos[1]][1] != side and not chess_board[pos[0] + m - 1][pos[1]]):
                possible_moves += [[pos[0] + m, pos[1]]]
            else:
                break

        for m in range(1, 8 - pos[1]):
            if not chess_board[pos[0]][pos[1] + m]:
                possible_moves += [[pos[0], pos[1] + m]]
            elif (m == 1 and chess_board[pos[0]][pos[1] + m][1] != side) or \
                    (chess_board[pos[0]][pos[1] + m][1] != side and not chess_board[pos[0]][pos[1] + m - 1]):
                possible_moves += [[pos[0], pos[1] + m]]
            else:
                break

        for m in range(1, pos[1] + 1):
            if not chess_board[pos[0]][pos[1] - m]:
                possible_moves += [[pos[0], pos[1] - m]]
            elif (m == 1 and chess_board[pos[0]][pos[1] - m][1] != side) or \
                    (chess_board[pos[0]][pos[1] - m][1] != side and not chess_board[pos[0]][pos[1] - m + 1]):
                possible_moves += [[pos[0], pos[1] - m]]
            else:
                break

        for m in range(1, pos[0] + 1):
            if not chess_board[pos[0] - m][pos[1]]:
                possible_moves += [[pos[0] - m, pos[1]]]
            elif (m == 1 and chess_board[pos[0] - m][pos[1]][1] != side) or \
                    (chess_board[pos[0] - m][pos[1]][1] != side and not chess_board[pos[0] - m + 1][pos[1]]):
                possible_moves += [[pos[0] - m, pos[1]]]
            else:
                break
        return possible_moves

    @staticmethod
    def bishop_moves(pos, side):
        possible_moves = []

        for p in range(1, 8):
            try:
                if not chess_board[pos[0] + p][pos[1] + p]:
                    possible_moves += [[pos[0] + p, pos[1] + p]]

                elif (p == 1 or not chess_board[pos[0] + p - 1][pos[1] + p - 1]) \
                        and chess_board[pos[0] + p][pos[1] + p][1] != side:
                    possible_moves += [[pos[0] + p, pos[1] + p]]
                else:
                    break
            except IndexError:
                break

        for p in range(1, 8):
            try:
                if not chess_board[pos[0] - p][pos[1] - p]:
                    possible_moves += [[pos[0] - p, pos[1] - p]]

                elif (p == 1 and chess_board[pos[0] - p][pos[1] - p][1] != side) or \
                        (chess_board[pos[0] - p][pos[1] - p][1] != side
                         and not chess_board[pos[0] - p + 1][pos[1] - p + 1]):
                    possible_moves += [[pos[0] - p, pos[1] - p]]
                else:
                    break
            except IndexError:
                break

        for p in range(1, 8):
            try:
                if not chess_board[pos[0] - p][pos[1] + p]:
                    possible_moves += [[pos[0] - p, pos[1] + p]]

                elif (p == 1 and chess_board[pos[0] - p][pos[1] + p][1] != side) or \
                        (chess_board[pos[0] - p][pos[1] + p][1] != side
                         and not chess_board[pos[0] - p + 1][pos[1] + p - 1]):
                    possible_moves += [[pos[0] - p, pos[1] + p]]
                else:
                    break
            except IndexError:
                break

        for p in range(1, 8):
            try:
                if not chess_board[pos[0] + p][pos[1] - p]:
                    possible_moves += [[pos[0] + p, pos[1] - p]]

                elif (p == 1 and chess_board[pos[0] + p][pos[1] - p][1] != side) or \
                        (chess_board[pos[0] + p][pos[1] - p][1] != side
                         and not chess_board[pos[0] + p - 1][pos[1] - p + 1]):
                    possible_moves += [[pos[0] + p, pos[1] - p]]
                else:
                    break
            except IndexError:
                break

        for p in sorted(possible_moves, reverse=True):
            if p not in chess_board_positions:
                del possible_moves[possible_moves.index(p)]

        return possible_moves

    @staticmethod
    def knight_moves(pos, side):
        possible_moves = []

        for m in [-2, 2]:
            for t in [-1, 1]:
                if [pos[0] + m, pos[1] + t] in chess_board_positions:
                    if not chess_board[pos[0] + m][pos[1] + t]:
                        possible_moves += [[pos[0] + m, pos[1] + t]]
                    elif chess_board[pos[0] + m][pos[1] + t][1] != side:
                        possible_moves += [[pos[0] + m, pos[1] + t]]

                if [pos[0] + t, pos[1] + m] in chess_board_positions:
                    if not chess_board[pos[0] + t][pos[1] + m]:
                        possible_moves += [[pos[0] + t, pos[1] + m]]
                    elif chess_board[pos[0] + t][pos[1] + m][1] != side:
                        possible_moves += [[pos[0] + t, pos[1] + m]]
        return possible_moves

    @staticmethod
    def queen_moves(pos, side):
        return ValidMoves.bishop_moves(pos, side) + ValidMoves.rook_moves(pos, side)

    # Test for a check is conducted in ...
    @staticmethod
    def king_moves(pos, side):
        possible_moves = []
        queen_moves = ValidMoves.queen_moves(pos, side)

        for q in queen_moves:
            if fabs(q[0] - pos[0]) <= 1 and fabs(q[1] - pos[1]) <= 1:
                possible_moves += [[q[0], q[1]]]

        return possible_moves

    @staticmethod
    def pawn_moves(pos, side):
        possible_moves = []

        if pos in [[y, 1] for y in range(0, 8)] and side == 'w':
            if not chess_board[pos[0]][pos[1] + 2] and not chess_board[pos[0]][pos[1] + 1]:
                possible_moves = [[pos[0], pos[1] + 1], [pos[0], pos[1] + 2]]
            elif not chess_board[pos[0]][pos[1] + 1]:
                possible_moves = [[pos[0], pos[1] + 1]]

        elif pos in [[y, 6] for y in range(0, 8)] and side == 'b':
            if not chess_board[pos[0]][pos[1] - 2] and not chess_board[pos[0]][pos[1] - 1]:
                possible_moves = [[pos[0], pos[1] - 1], [pos[0], pos[1] - 2]]
            elif not chess_board[pos[0]][pos[1] - 1]:
                possible_moves = [[pos[0], pos[1] - 1]]

        # Check whether the pawn can eat
        elif side == 'w' and not chess_board[pos[0]][pos[1] + 1]:
            possible_moves = [[pos[0], pos[1] + 1]]
        elif side == 'b' and not chess_board[pos[0]][pos[1] - 1]:
            possible_moves = [[pos[0], pos[1] - 1]]

        # Check whether the pawn can attack enemy piece(s)
        if [pos[0] + 1, pos[1] + 1] in chess_board_positions:
            if chess_board[pos[0] + 1][pos[1] + 1] and side == 'w':
                if chess_board[pos[0] + 1][pos[1] + 1][1] != side:
                    possible_moves += [[pos[0] + 1, pos[1] + 1]]

        if [pos[0] - 1, pos[1] + 1] in chess_board_positions:
            if chess_board[pos[0] - 1][pos[1] + 1] and side == 'w':
                if chess_board[pos[0] - 1][pos[1] + 1][1] != side:
                    possible_moves += [[pos[0] - 1, pos[1] + 1]]

        if [pos[0] - 1, pos[1] - 1] in chess_board_positions:
            if chess_board[pos[0] - 1][pos[1] - 1] and side == 'b':
                if chess_board[pos[0] - 1][pos[1] - 1][1] != side:
                    possible_moves += [[pos[0] - 1, pos[1] - 1]]

        if [pos[0] + 1, pos[1] - 1] in chess_board_positions:
            if chess_board[pos[0] + 1][pos[1] - 1] and side == 'b':
                if chess_board[pos[0] + 1][pos[1] - 1][1] != side:
                    possible_moves += [[pos[0] + 1, pos[1] - 1]]

        return possible_moves


class Checker(object):
    def __init__(self, side):
        self.side = side

    def king_finder(self):
        for u in range(8):
            for y in range(8):
                if chess_board[u][y]:
                    if chess_board[u][y][1] == self.side[1] and chess_board[u][y][0] == 'K':
                        return [u, y]

    def is_check(self):
        king_pos = Checker.king_finder(self)
        for u in range(8):
            for y in range(8):
                if chess_board[u][y]:
                    if chess_board[u][y][1] != self.side[1]:
                        enemy_piece_moves = ValidMoves([u, y])
                        if king_pos in enemy_piece_moves.get_moves():
                            return True
        return False

    def is_mate_or_stalemate(self):
        if Checker.is_check(self):
            result = 'M'
            # If any move on the board you can make saves you from check then it's not a mate
            for u in range(8):
                for y in range(8):
                    if chess_board[u][y]:
                        if chess_board[u][y][1] == self.side[1]:
                            positions = ValidMoves([u, y])

                            for t in positions.get_moves():
                                piece_on_to_pos = chess_board[t[0]][t[1]]

                                chess_board[t[0]][t[1]] = chess_board[u][y]
                                chess_board[u][y] = None

                                if not Checker.is_check(self):
                                    result = False

                                chess_board[u][y] = chess_board[t[0]][t[1]]
                                chess_board[t[0]][t[1]] = piece_on_to_pos
        else:
            result = 'S'
            # If you can make any move on the board without being checked then it's not a stalemate
            for u in range(8):
                for y in range(8):
                    if chess_board[u][y]:
                        if chess_board[u][y][1] == self.side[1]:
                            positions = ValidMoves([u, y])
                            for t in positions.get_moves():
                                piece_on_to_pos = chess_board[t[0]][t[1]]

                                chess_board[t[0]][t[1]] = chess_board[u][y]
                                chess_board[u][y] = None

                                if not Checker.is_check(self):
                                    result = False

                                chess_board[u][y] = chess_board[t[0]][t[1]]
                                chess_board[t[0]][t[1]] = piece_on_to_pos
        return result
