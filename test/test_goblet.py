import unittest
import sys, os
from unittest.mock import MagicMock
sys.path.append(os.path.join(os.getcwd(), "src"))

from Game import *

class BoardTest(unittest.TestCase):
    def test_get_board_and_can_put_list(self):
        #case 1
        board = Board()

        board.players["first"].get_own_board = MagicMock(return_value = [[3, 0, 0], [0, 0, 3], [1, 1, 0]])
        board.players["second"].get_own_board = MagicMock(return_value = [[0, 0, 0], [2, 0, 0], [0, 3, 0]])

        ecpected = [[3, 0, 0], [-2, 0, 3], [1, -3, 0]]
        actual = board.get_board()

        self.assertEqual(ecpected, actual)

        ecpected = [[0, 1], [0, 2], [1, 1], [2, 2]]
        actual = board.get_can_put_list("small")

        self.assertEqual(ecpected, actual)

        ecpected = [[0, 1], [0, 2], [1, 1], [2, 0], [2, 2]]
        actual = board.get_can_put_list("middle")

        self.assertEqual(ecpected, actual)

        ecpected = [[0, 1], [0, 2], [1, 0], [1, 1], [2, 0], [2, 2]]
        actual = board.get_can_put_list("large")

        self.assertEqual(ecpected, actual)

    # 未完成
    def test_get_can_put_list():
        board = Board()

        board.players["first"].get_unused_stones = MagicMock(return_value = ["small", "middle"])

        def mock_return_value(*args, **kwargs):
            if args[0] == "small":
                return [[0, 1], [0, 2], [1, 1], [2, 2]]
            elif args[0] == "middle":
                return [[0, 1], [0, 2], [1, 1], [2, 0], [2, 2]]
            
        board.get_can_put_list = MagicMock(side_effect = mock_return_value)

        board.get_board = MagicMock(return_value = [[3, 0, 0], [-2, 0, 3], [1, -3, 0]])

class PlayerTest(unittest.TestCase):
    def test_get_unused_stones(self):
        # case 1
        player = Player(1, 1, 1)

        ecpected = ["small", "middle", "large"]
        actual = player.get_unused_stones()

        self.assertEqual(ecpected, actual)

        #case 2
        player = Player(0, 1, 1)

        ecpected = ["middle", "large"]
        actual = player.get_unused_stones()
        
        self.assertEqual(ecpected, actual)

        #case 3
        player = Player(0, 0, 0)

        ecpected = []
        actual = player.get_unused_stones()
        
        self.assertEqual(ecpected, actual)

    def test_get_own_board(self):
        # case 1
        player = Player(1, 1, 1)
        player.stones["small"] = [[1, 0, 0], [1, 0, 0], [0, 0, 1]]
        player.stones["middle"] = [[1, 0, 0], [0, 1, 0], [1, 0, 0]]
        player.stones["large"] = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

        ecpected = [[3, 0, 0], [3, 2, 0], [3, 0, 1]]
        actual = player.get_own_board()

        # case 2
        player = Player(1, 1, 1)
        player.stones["small"] = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
        player.stones["middle"] = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
        player.stones["large"] = [[0, 0, 1], [0, 0, 1], [0, 0, 1]]

        ecpected = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        actual = player.get_own_board()

        self.assertEqual(ecpected, actual)

class TypeOfStoneTest(unittest.TestCase):
    def test_change_stone(self):
        # case 1
        type_of_stone = TypeOfStone(1)
        type_of_stone.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        type_of_stone.change_stone(1, 1)

        ecpected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        actual = type_of_stone.board

        self.assertEqual(ecpected, actual)

        # case 2
        type_of_stone = TypeOfStone(1)
        type_of_stone.board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

        type_of_stone.change_stone(1, 1)

        ecpected = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        actual = type_of_stone.board

        self.assertEqual(ecpected, actual)    

if __name__ == '__main__':
    unittest.main()
