from project import player_has_won
from project import board_is_full

def test_player_has_won():
    board = [['x', 'o', 'x'], ['o', 'x', 'o'], ['x', 'o', 'x']]
    assert player_has_won(board)

def test_board_is_full():
    board = board = [['x', 'o', 'x'], ['o', 'x', 'o'], ['x', 'o', 'x']]
    assert board_is_full(board)