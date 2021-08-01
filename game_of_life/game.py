import logging
import copy

logging.basicConfig(filename='foo.log', level=logging.DEBUG)
logging.debug("hello")


class Game:
    """defines an instance of the game of life"""

    def __init__(self):
        """initialize an empty board"""
        self.board = list(list(0 for _ in range(20)) for _ in range(20))
        self.next_board = list(list(0 for _ in range(20)) for _ in range(20))

    def board_to_string(self):
        s = ""
        for row in self.board:
            for column in row:
                if column == 0:
                    s += " "
                if column == 1:
                    s += "*"
            s += '\n'
        return s

    def set_cell_alive(self, row, column):
        self.board[row][column] = 1

    def set_cell_dead(self, row, column):
        self.board[row][column] = 0

    def advance_to_next_generation(self):
        for row_num, row in enumerate(self.board):
            for col_num, column in enumerate(row):
                if self.board[row_num][col_num] == 1:
                    if 2 <= self.count_neighbors(row_num, col_num) <= 3:
                        self.next_board[row_num][col_num] = 1
                    else:
                        self.next_board[row_num][col_num] = 0
                elif self.board[row_num][col_num] == 0:
                    if self.count_neighbors(row_num, col_num) == 3:
                        self.next_board[row_num][col_num] = 1
                    else:
                        self.next_board[row_num][col_num] = 0
        # copy values of next generation onto current generation
        self.board = copy.deepcopy(self.next_board)

    def count_neighbors(self, row_num, col_num):
        count = 0
        logging.warning("hello 82572")
        for row_num_to_check in range(row_num-1, row_num+2):
            # logging.warning('row_num_to_check: ' + str(row_num_to_check))
            for col_num_to_check in range(col_num-1, col_num+2):

                # logging.warning('col_num_to_check: ' + str(col_num_to_check))
                # logging.warning('not (row_num_to_check == row_num and col_num_to_check == col_num) ' + str(not (row_num_to_check == row_num and col_num_to_check == col_num)))
                if not (row_num_to_check == row_num and col_num_to_check == col_num):
                    logging.warning('checking row_num_to_check ' + str(row_num_to_check) + ' and col_num_to_check ' + str(col_num_to_check))
                    try:
                        if self.board[row_num_to_check][col_num_to_check] == 1:
                            logging.warning('adding one to the count')
                            count += 1
                    except IndexError:
                        pass  # act as if cells beyond the boundary are dead
                        # todo just for fun, try it later as if all cells beyond the boundary are alive
        return count

