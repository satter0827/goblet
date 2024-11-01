import random
import Statics
    
class Player():
    def __init__(self, num_of_small=Statics.NUM_OF_SMALL_PIECES, num_of_middle=Statics.NUM_OF_MIDDLE_PIECES, num_of_large=Statics.NUM_OF_LARGE_PIECES):
        self.stones = {
            "small": TypeOfStone(num_of_small),
            "middle": TypeOfStone(num_of_middle),
            "large": TypeOfStone(num_of_large),
        }

    def get_unused_stones(self):
        list_of_unused_stones = []

        for type, stone in self.stones.items():
            if stone.num > 0:
                list_of_unused_stones.append(type)
                
        return list_of_unused_stones
    
    def get_own_board(self):
        own_board = [[0 for _ in range(Statics.BOARD_SIZE)] for _ in range(Statics.BOARD_SIZE)]

        for row in range(Statics.BOARD_SIZE):
            for col in range(Statics.BOARD_SIZE):
                if self.stones["small"][row][col] == 1:
                    own_board[row][col] = Statics.STONE_ID["small"]

                if self.stones["middle"][row][col] == 1:
                    own_board[row][col] = Statics.STONE_ID["middle"]
                
                if self.stones["large"][row][col] == 1:
                    own_board[row][col] = Statics.STONE_ID["large"]

        return own_board


class TypeOfStone():
    """
    Gobletにおける石を定義する
    """
    
    def __init__(self, num_of_stones:int):
        """
        コンストラクタ

        Args:
            num_of_stones(int):石の個数
        """

        # 石の数を定義する
        self.num_of_stones = num_of_stones

        # 石単位のボードをOFFで初期化する
        self.board = [[Statics.Stone.OFF for _ in range(Statics.BOARD_SIZE)] for _ in range(Statics.BOARD_SIZE)]

    def change_stone(self, iRow:int, iCol:int) -> None:
        """
        引数で指定した石を反転させる

        引数:
            iRow(int):行
            iCol(int):列
        """

        #　反転処理
        if self.board[iRow][iCol] == Statics.Stone.OFF:
            # OFF → ON
            self.board[iRow][iCol] = Statics.Stone.ON
        elif self.board[iRow][iCol] == Statics.Stone.ON:
            # ON →O FF
            self.board[iRow][iCol] = Statics.Stone.OFF

class Board():
    def __init__(self, num_of_small=Statics.NUM_OF_SMALL_PIECES, num_of_middle=Statics.NUM_OF_MIDDLE_PIECES, num_of_large=Statics.NUM_OF_LARGE_PIECES):
        self.players = {
            "first": Player(num_of_small, num_of_middle, num_of_large),
            "second": Player(num_of_small, num_of_middle, num_of_large),
        }

    def get_can_move_list(self, current_player):
        can_move_list = []
        unused_stones = self.players[current_player].get_unused_stones()

        for unused_stone in unused_stones:
            can_put_list = self.get_can_put_list(unused_stone)
            can_move_list.append([unused_stone, -1, -1, can_put_list])

        current_board = self.get_board()
        
        for row in range(Statics.BOARD_SIZE):
            for col in range(Statics.BOARD_SIZE):
                target_stone = current_board[row][col] * Statics.PLAYER_ID[current_player]
                put_stone = None

                if target_stone > 0:
                    if target_stone == Statics.STONE_ID["small"]:
                        put_stone = target_stone
                    elif target_stone == Statics.STONE_ID["middle"]:
                        put_stone = target_stone
                    elif target_stone == Statics.STONE_ID["large"]:
                        put_stone = target_stone

                if put_stone is not None:
                    can_put_list = self.get_can_put_list(put_stone)
                    can_move_list.append([put_stone, row, col, can_put_list])

        return can_move_list
    
    def get_can_put_list(self, stone_name):
        current_board = self.get_board()
        can_put_list = []

        for row in range(Statics.BOARD_SIZE):
            for col in range(Statics.BOARD_SIZE):
                if Statics.STONE_ID[stone_name] > abs(current_board[row][col]):
                    can_put_list.append([row, col])

        return can_put_list
    
    def get_board(self):
        marged_board = [[0 for _ in range(Statics.BOARD_SIZE)] for _ in range(Statics.BOARD_SIZE)]

        board_of_first_player = self.players["first"].get_own_board()
        board_of_second_player = self.players["second"].get_own_board()

        for row in range(Statics.BOARD_SIZE):
            for col in range(Statics.BOARD_SIZE):
                if board_of_first_player[row][col] > board_of_second_player[row][col]:
                    marged_board[row][col] = board_of_first_player[row][col]
                elif board_of_first_player[row][col] < board_of_second_player[row][col]:
                    marged_board[row][col] = -board_of_second_player[row][col]

        return marged_board
    
    def put_stone_randomly(self, player):
        can_move_list = self.get_can_move_list(player)

        return random.choice(can_move_list)
    
    def check_end(self, player):
        current_board = self.get_board()

        # 縦
        for row in range(Statics.BOARD_SIZE):
            if Statics.PLAYER_ID[player] * current_board[row][0] > 0 \
                and Statics.PLAYER_ID[player] * current_board[row][1] > 0 \
                and Statics.PLAYER_ID[player] * current_board[row][2] > 0:

                return True

        return False

if __name__ == "__main__":
    goblet = Goblet()
    goblet.play_game()