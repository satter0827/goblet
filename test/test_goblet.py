import unittest
import sys, os
sys.path.append(os.path.join(os.getcwd(), "src"))

from Game import *

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
