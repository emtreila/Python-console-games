import unittest

from repository.repository import MemoRepo
from service.service import Service


class TestService(unittest.TestCase):

    def setUp(self):
        self._repository = MemoRepo()
        self._service = Service(self._repository)

    def test_board(self):
        # check if the board is created correctly
        board = self._repository.board
        self.assertEqual(len(board), 6, "The row length should be 6!")
        self.assertEqual(len(board[0]), 7, "The column length should be 7!")

        self._repository.board = [[2, 1, 1, 2, 2, 0, 1, ],
                                  [0, 2, 1, 1, 1, 2, 1, ],
                                  [0, 2, 2, 1, 2, 0, 2, ],
                                  [0, 1, 1, 0, 2, 0, 0, ],
                                  [0, 1, 0, 0, 1, 0, 0, ],
                                  [0, 0, 0, 0, 1, 0, 0, ]]

        # check if there is a valid location
        self.assertTrue(self._service.is_valid_location(0), "The location should be valid!")
        self.assertFalse(self._service.is_valid_location(4), "The location should be invalid!")

        # check if the open row is returned correctly
        self.assertEqual(self._service.get_open_row(0), 1, "The open row should be 1!")

        # check if the piece is put on the board correctly
        self._service.put_piece(5, 1, 1)
        self.assertEqual(self._repository.board[5][1], 1, "The piece should be 1!")

    def check_winning(self):
        self._repository.board = [[2, 1, 1, 2, 2, 0, 1, ],
                                  [0, 2, 1, 1, 1, 2, 1, ],
                                  [0, 2, 2, 1, 2, 0, 2, ],
                                  [0, 1, 1, 0, 2, 0, 0, ],
                                  [0, 1, 0, 0, 1, 0, 0, ],
                                  [0, 0, 0, 0, 1, 0, 0, ]]

        # check if the game is won
        self.assertTrue(self._service.is_won(1), "The game should be won!")

        # check if the game ends in a tie
        self._repository.board = [[2, 1, 1, 2, 2, 1, 1, ],
                                  [1, 2, 1, 1, 1, 2, 1, ],
                                  [2, 2, 2, 1, 2, 1, 2, ],
                                  [1, 1, 1, 2, 2, 1, 1, ],
                                  [2, 1, 2, 1, 1, 2, 2, ],
                                  [1, 2, 1, 2, 1, 2, 1, ]]

        self.assertTrue(self._service.is_tie(), "The game should end in a tie!")

        # check the next winning move for the computer
        self._repository.board = [[2, 1, 1, 2, 2, 0, 1, ],
                                  [0, 2, 1, 1, 1, 2, 1, ],
                                  [0, 2, 2, 1, 2, 0, 2, ],
                                  [0, 1, 0, 0, 2, 0, 0, ],
                                  [0, 0, 0, 0, 1, 0, 0, ],
                                  [0, 0, 0, 0, 1, 0, 0, ]]

        self.assertEqual(self._service.winning_move_computer(), (3, 3), "The winning move should be row 3 column 3!")

        # check the next winning move for the user
        self._repository.board = [[2, 1, 1, 2, 2, 0, 1, ],
                                  [0, 2, 1, 1, 1, 2, 1, ],
                                  [0, 2, 2, 1, 2, 0, 2, ],
                                  [0, 1, 1, 0, 2, 0, 0, ],
                                  [0, 0, 0, 0, 1, 0, 0, ],
                                  [0, 0, 0, 0, 1, 0, 0, ]]

        self.assertEqual(self._service.winning_move_user(), (4, 1), "The winning move should be row 4 column 1!")
