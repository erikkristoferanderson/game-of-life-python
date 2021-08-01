# import pytest
from mygamefile import Game
import resources


def test_init():
    game = Game()
    assert game.board == resources.EMPTY_BOARD
    assert game.next_board == resources.EMPTY_BOARD


def test_print_empty_board():
    game = Game()
    assert game.board_to_string() == resources.EMPTY_BOARD_STRING


def test_set_cell_alive():
    game = Game()
    game.set_cell_alive(2, 4)
    assert game.board == resources.BOARD_WITH_ROW_2_COLUMN_4_ALIVE


def test_print_board_with_row_2_column_4_alive():
    game = Game()
    game.set_cell_alive(2, 4)
    s = game.board_to_string()
    assert s == resources.BOARD_WITH_ROW_2_COLUMN_4_ALIVE_STRING


def test_set_cell_dead():
    game = Game()
    game.set_cell_alive(2, 4)
    game.set_cell_dead(2, 4)
    assert game.board == resources.EMPTY_BOARD

def test_swap_life_state():
    game = Game()
    game.set_cell_alive(2, 4)
    game.swap_life_state(2, 4)
    assert game.board == resources.EMPTY_BOARD
    game.swap_life_state(2, 4)
    assert game.board == resources.BOARD_WITH_ROW_2_COLUMN_4_ALIVE

def test_count_neighbors():
    game = Game()
    game.set_cell_alive(2, 4)
    assert game.count_neighbors(2, 4) == 0
    assert game.count_neighbors(1, 4) == 1


def test_next_generation_of_empty_board():
    game = Game()
    game.advance_to_next_generation()
    assert game.board == resources.EMPTY_BOARD


def test_next_generation_of_board_with_row_2_column_4_alive():
    game = Game()
    game.board = resources.BOARD_WITH_ROW_2_COLUMN_4_ALIVE_STRING
    game.advance_to_next_generation()
    assert game.board == resources.EMPTY_BOARD


def test_next_generation_of_board_with_square():
    game = Game()
    game.board = resources.BOARD_WITH_SQUARE_AT_ROW_2_COLUMN_4_ALIVE


def test_blinker_boards():
    game = Game()
    game.board = resources.BOARD_WITH_BLINKER_A
    game.advance_to_next_generation()
    assert game.board == resources.BOARD_WITH_BLINKER_B
    game.advance_to_next_generation()
    assert game.board == resources.BOARD_WITH_BLINKER_A
