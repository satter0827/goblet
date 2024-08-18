import Statics

class Goblet():
    board = None
    game_status = None
    piece_of_player = None
    current_player = None
    turn = None

    def play_game(self):
        self.board = {
            "small_stone_board": [[0 for _ in range(Statics.ROWS_OF_BOARD)] for _ in range(Statics.COLUMNS_OF_BOARD)],
            "middle_stone_board": [[0 for _ in range(Statics.ROWS_OF_BOARD)] for _ in range(Statics.COLUMNS_OF_BOARD)],
            "large_stone_board": [[0 for _ in range(Statics.ROWS_OF_BOARD)] for _ in range(Statics.COLUMNS_OF_BOARD)],
        }

        self.piece_of_player = {
            "first_player": {
                "num_small_stones": 3,
                "num_middle_stones": 3,
                "num_large_stones": 3,
            },
            "second_player": {
                "num_small_stones": 3,
                "num_middle_stones": 3,
                "num_large_stones": 3,
            },
        }

        self.game_status = {
            "first_player": {
                "small"
            },
            "second_player": {

            },
        }

        self.urrent_player = Statics.FIRST_TURN

        self.turn = 0

        print("start")

        current_player = Statics.FIRST_TURN
        can_move_list = self.get_can_move_list(current_player)
        print(can_move_list)

        current_player = Statics.SECOND_TURN
        can_move_list = self.get_can_move_list(current_player)
        print(can_move_list)

        print("end")

    def get_can_move_list(self, current_player):
        can_move_list = None
        piece_of_current_player = None

        if current_player == 0:
            piece_of_current_player = self.piece_of_player["first_player"]
        else:
            piece_of_current_player = self.piece_of_player["second_player"]

        for key, num_of_stone in piece_of_current_player.items():
            if num_of_stone > 0:
                stone_id = None

                if key == "num_small_stones":
                    stone_id = 1
                elif key == "num_middle_stones":
                    stone_id = 2
                elif key == "num_large_stones":
                    stone_id = 3

                print(stone_id)

                for row in range(3):
                    for col in range(3):
                        if self.board["small_stone_board"][row][col] < stone_id and self.board["small_stone_board"][row][col] < stone_id and self.board["small_stone_board"][row][col] < stone_id:
                            can_move_list.append([stone_id, -1, -1, row, col])

        return 0
    
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
        own_board = [[0 for _ in range(Statics.ROWS_OF_BOARD)] for _ in range(Statics.COLUMNS_OF_BOARD)]

        for row in range(Statics.ROWS_OF_BOARD):
            for col in range(Statics.COLUMNS_OF_BOARD):
                if self.stones["small"][row][col] == 1:
                    own_board[row][col] = Statics.SMALL_STONE_ID

                if self.stones["middle"][row][col] == 1:
                    own_board[row][col] = Statics.MIDDLE_STONE_ID
                
                if self.stones["large"][row][col] == 1:
                    own_board[row][col] = Statics.LARGE_STONE_ID

        return own_board

class TypeOfStone():
    def __init__(self, num):
        self.num = num
        self.board = [[0 for _ in range(Statics.ROWS_OF_BOARD)] for _ in range(Statics.COLUMNS_OF_BOARD)]

    def change_stone(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = 1
        elif self.board[row][col] == 1:
            self.board[row][col] = 0
        else:
            raise


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
            can_put_list = self.get_can_move_list(current_player, unused_stone)
            can_move_list.append([unused_stone, -1, -1, can_put_list])

        return can_move_list
    
    def get_can_put_list(self, current_player, type_of_stone):
        can_put_list = []

        for row in range(Statics.ROWS_OF_BOARD):
            for col in range(Statics.COLUMNS_OF_BOARD):
                if self.players["first"][row][col] < 0:
                    pass

        return can_put_list
    
    def get_board(self):
        marged_board = [[0 for _ in range(Statics.ROWS_OF_BOARD)] for _ in range(Statics.COLUMNS_OF_BOARD)]

        for move in ["first", "second"]:
            puted_stone = 0

            if self.players["first"]:
                pass

        return marged_board

if __name__ == "__main__":
    goblet = Goblet()
    goblet.play_game()