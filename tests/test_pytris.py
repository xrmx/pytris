from unittest import TestCase

from pytris.lib import init_board, move, row, col, oblique, won, win, full, EndGame


class SampleTestCase(TestCase):
    def test_init_board_return_a_3x3_board(self):
        board = init_board()
        self.assertEqual(len(board), 3)
        self.assertEqual(len(board[0]), 3)
        self.assertEqual(len(board[1]), 3)
        self.assertEqual(len(board[2]), 3)
        self.assertFalse(any(board[0]))
        self.assertFalse(any(board[1]))
        self.assertFalse(any(board[2]))

    def test_move_does_move(self):
        board = init_board()
        first_move = move(board, 0, 0, 'x')
        self.assertTrue(first_move)
        self.assertEqual(board[0][0], 'x')

    def test_move_does_not_permit_override(self):
        board = init_board()
        first_move = move(board, 0, 0, 'x')
        second_move = move(board, 0, 0, 'x')
        self.assertFalse(second_move)

    def test_row_serializes_row(self):
        board = init_board()
        board[0][0] = 'x'
        self.assertEqual(row(board, 0), 'x')

    def test_col_serializes_column(self):
        board = init_board()
        board[0][0] = 'x'
        self.assertEqual(col(board, 0), 'x')

    def test_oblique_serializes_oblique(self):
        board = init_board()
        board[0][0] = board[0][2] = 'x'
        self.assertEqual(oblique(board, 0), 'x')
        self.assertEqual(oblique(board, 1), 'x')

    def test_won_recognize_player_one_win(self):
        self.assertTrue(won('xxx'))

    def test_won_recognize_player_two_win(self):
        self.assertTrue(won('ooo'))

    def test_won_recognize_no_win(self):
        self.assertFalse(won('xo'))

    def test_win_find_winner_in_board_row(self):
        board = init_board()
        board[0][0] = board[0][1] = board[0][2] = 'x'
        ret, winner = win(board)
        self.assertTrue(ret)

    def test_win_find_winner_in_board_col(self):
        board = init_board()
        board[0][0] = board[1][0] = board[2][0] = 'x'
        ret, winner = win(board)
        self.assertTrue(ret)

    def test_win_find_winner_in_board_first_oblique(self):
        board = init_board()
        board[0][0] = board[1][1] = board[2][2] = 'x'
        ret, winner = win(board)
        self.assertTrue(ret)

    def test_win_find_winner_in_board_second_oblique(self):
        board = init_board()
        board[0][2] = board[1][1] = board[2][0] = 'x'
        ret, winner = win(board)
        self.assertTrue(ret)

    def test_win_find_no_winner_in_empty_board(self):
        board = init_board()
        ret, winner = win(board)
        self.assertFalse(ret)

    def test_full_raise_end_game_on_board_full(self):
        board = init_board()
        for i in range(3):
            for j in range(3):
                board[i][j] = 'x'
        with self.assertRaises(EndGame):
            full(board)

    def test_full_returns_none_on_not_full_board(self):
        board = init_board()
        self.assertIsNone(full(board))
