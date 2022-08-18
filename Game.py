from textwrap import dedent
from Engine import *

# To-do: CASTLING and En passant! Thus database of moves
# To-do: decode classical way of inputting moves


class Start(object):
    def __init__(self, validator, checker):
        self.validator_from = validator
        self.checker = checker

    def main(self):
        previous_move_side = []

        print(dedent("""
                        When you are asked to make a move input 2 numbers with a space between them,
                        the first one is position on X axis the second - on Y.
                        Castling and En passant mechanics are currently under development.
                        """))

        while True:
            Start.print_chessboard()

            from_pos_string = input(f"{self.checker.side[0]} moves from position: ")
            to_pos_string = input("To position: ")

            # Validates and converts the input
            try:
                self.validator_from = ValidMoves([int(p) - 1 for p in from_pos_string.split(' ')])
                to_pos = [int(p) - 1 for p in to_pos_string.split(' ')]
            except (ValueError, TypeError, IndexError):
                print("Invalid input.")
                print("Input 2 numbers within range of 1 and 8 on X and Y axis accordingly putting space between them.")
                continue
            if to_pos not in chess_board_positions:
                print("Invalid input.")
                print("Input 2 numbers within range of 1 and 8 on X and Y axis accordingly putting space between them.")
                continue

            # If a move is successful, it changes who's move is now
            if not Start.move(self, to_pos):
                continue

            if self.checker.side[1] == 'w':
                self.checker = Checker(['Black', 'b'])
                previous_move_side = 'White'
            elif self.checker.side[1] == 'b':
                self.checker = Checker(['White', 'w'])
                previous_move_side = 'Black'

            # Checks for mate and stalemate
            mate_or_stalemate = self.checker.is_mate_or_stalemate()
            if mate_or_stalemate == 'M':
                Start.print_chessboard()
                exit(f"{previous_move_side} wins!")
            elif mate_or_stalemate == 'S':
                Start.print_chessboard()
                exit("Stalemate!")

    @staticmethod
    def print_chessboard():
        print('\t', end='')
        for t in range(8):
            print("_____", end='')
        print('_')

        for b in range(7, -1, -1):
            print(f"  {b + 1}", end=' ')
            for r in range(8):
                if type(chess_board[r][b]) is list:
                    print(f"| {chess_board[r][b][1]}{chess_board[r][b][0]} ", end='')
                else:
                    print("|    ", end='')
            print('|')

            print('\t', end='')
            for t in range(8):
                print("|____", end='')
            print('|')

        print('\t  ', end='')
        for t in range(1, 9):
            print("{: ^4}".format(str(t)), end=' ')

        print('\n')

    def move(self, to_pos):
        # Checks for invalid input
        try:
            if chess_board[self.validator_from.pos[0]][self.validator_from.pos[1]][1] != self.checker.side[1]:
                print("Invalid input position. You can't move opponent's pieces.")
                return None
            elif to_pos not in self.validator_from.get_moves():
                print("Invalid input. You can't move to this square with given piece.")
                return None
        except ValueError:
            print("Invalid input position.")
            return None

        # First it makes a move
        piece_on_to_pos = chess_board[to_pos[0]][to_pos[1]]
        chess_board[to_pos[0]][to_pos[1]] = chess_board[self.validator_from.pos[0]][self.validator_from.pos[1]]
        chess_board[self.validator_from.pos[0]][self.validator_from.pos[1]] = None

        # And then returns it if it's invalid
        if self.checker.is_check():
            print('Invalid move. The King is under attack.')
            chess_board[self.validator_from.pos[0]][self.validator_from.pos[1]] = chess_board[to_pos[0]][to_pos[1]]
            chess_board[to_pos[0]][to_pos[1]] = piece_on_to_pos
            return None

        # Converts pawns into preferred pieces when they reach the end of the board
        for h in range(8):
            if chess_board[h][7]:
                if chess_board[h][7][0] == 'p' and chess_board[h][7][1] == self.checker.side[1]:
                    while True:
                        turn_into = input(f"What to turn white pawn on ({h + 1} 8) into? Input Q, R, B or N\n")
                        if turn_into in ['Q', 'R', 'B', 'N']:
                            chess_board[h][7][0] = turn_into
                            break
                        else:
                            print("Q for Queen, R for Rook, B for Bishop, and N for Knight")

        return 'Done'


validator_go = ValidMoves([0, 0])
checker_go = Checker(['White', 'w'])
starter = Start(validator_go, checker_go)

starter.main()
