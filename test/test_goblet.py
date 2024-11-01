import unittest
import sys, os

from parameterized import parameterized
from unittest.mock import MagicMock
sys.path.append(os.path.join(os.getcwd(), "src"))

from Domain import *
import Statics

class BoardTest(unittest.TestCase):
    @parameterized.expand([
        # case 1
        (
            [[3, 0, 0], [0, 0, 3], [1, 1, 0]],
            [[0, 0, 0], [2, 0, 0], [0, 3, 0]],
            [[3, 0, 0], [-2, 0, 3], [1, -3, 0]],
            [[0, 1], [0, 2], [1, 1], [2, 2]],
            [[0, 1], [0, 2], [1, 1], [2, 0], [2, 2]],
            [[0, 1], [0, 2], [1, 0], [1, 1], [2, 0], [2, 2]]
        )
    ])
    def test_get_board_and_can_put_list(self, mock_1, mock_2, ecpected_1, ecpected_2, ecpected_3, ecpected_4):
        board = Board()

        board.players["first"].get_own_board = MagicMock(return_value = mock_1)
        board.players["second"].get_own_board = MagicMock(return_value = mock_2)

        actual = board.get_board()
        self.assertEqual(ecpected_1, actual)

        actual = board.get_can_put_list("small")
        self.assertEqual(ecpected_2, actual)

        actual = board.get_can_put_list("middle")
        self.assertEqual(ecpected_3, actual)

        actual = board.get_can_put_list("large")
        self.assertEqual(ecpected_4, actual)

    # 未完成
    def test_get_can_put_list(self):
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
    @parameterized.expand([
        (Player(1, 1, 1), ["small", "middle", "large"]),
        (Player(0, 1, 1), ["middle", "large"]),
    ])
    def test_get_unused_stones(self, player, ecpected):
        player = player

        actual = player.get_unused_stones()

        self.assertEqual(ecpected, actual)

    @parameterized.expand([
        (Player(1, 1, 1), [[1, 0, 0], [1, 0, 0], [0, 0, 1]], [[1, 0, 0], [0, 1, 0], [1, 0, 0]], [[1, 0, 0], [1, 0, 0], [1, 0, 0]], [[3, 0, 0], [3, 2, 0], [3, 0, 1]]),
        (Player(1, 1, 1), [[1, 0, 0], [1, 0, 0], [1, 0, 0]], [[0, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 1], [0, 0, 1], [0, 0, 1]], [[1, 2, 3], [1, 2, 3], [1, 2, 3]]),
    ])
    def test_get_own_board(self, player, stones_of_small, stones_of_middle, stones_of_large, expected):
        player = Player(1, 1, 1)
        player.stones["small"] = stones_of_small
        player.stones["middle"] = stones_of_middle
        player.stones["large"] = stones_of_large

        ecpected = expected
        actual = player.get_own_board()

class TypeOfStoneTest(unittest.TestCase):
    # テストケース
    test_list = []
    
    # case 1
    num_of_stones = 1
    test_board = [
        [Statics.Stone.OFF, Statics.Stone.OFF, Statics.Stone.OFF], 
        [Statics.Stone.OFF, Statics.Stone.OFF, Statics.Stone.OFF],
        [Statics.Stone.OFF, Statics.Stone.OFF, Statics.Stone.OFF]
    ]
    row = 1
    col = 1
    expected = [
        [Statics.Stone.OFF, Statics.Stone.OFF, Statics.Stone.OFF], 
        [Statics.Stone.OFF, Statics.Stone.ON, Statics.Stone.OFF],
        [Statics.Stone.OFF, Statics.Stone.OFF, Statics.Stone.OFF]
    ]

    test_list.append((num_of_stones, test_board, row, col, expected))

    # case 2
    num_of_stones = 1
    test_board = [
        [Statics.Stone.ON, Statics.Stone.ON, Statics.Stone.ON], 
        [Statics.Stone.ON, Statics.Stone.ON, Statics.Stone.ON],
        [Statics.Stone.ON, Statics.Stone.ON, Statics.Stone.ON]
    ]
    row = 1
    col = 1
    expected = [
        [Statics.Stone.ON, Statics.Stone.ON, Statics.Stone.ON], 
        [Statics.Stone.ON, Statics.Stone.OFF, Statics.Stone.ON],
        [Statics.Stone.ON, Statics.Stone.ON, Statics.Stone.ON]
    ]

    test_list.append((num_of_stones, test_board, row, col, expected))

    @parameterized.expand([case for case in test_list])
    def test_change_stone(self, num_of_stones, board, row, col, expected):
        # 石の個数を設定
        type_of_stone = TypeOfStone(num_of_stones)
        type_of_stone.board = board

        # 石を反転させる
        type_of_stone.change_stone(row, col)

        # 結果を取得
        actual = type_of_stone.board

        # 評価
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
