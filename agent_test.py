"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        # create an isolation board (by default 7x7)
        self.player1 = game_agent.MinimaxPlayer()
        self.player2 = game_agent.MinimaxPlayer()
        self.game = isolation.Board(self.player1, self.player2)
        self.game._board_state = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 68, 32]

    
    def test_solve(self):
        # place player 1 on the board at row 2, column 3, then place player 2 on
        # the board at row 0, column 5; display the resulting board state.  Note
        # that the .apply_move() method changes the calling object in-place.
        self.game.apply_move((2, 3))
        self.game.apply_move((0, 5))
        print(self.game.to_string())

        # players take turns moving on the board, so player1 should be next to move
        self.assertEqual(self.player1, self.game.active_player)

if __name__ == '__main__':
    unittest.main()
