class Goblet():
    board = None
    game_status = None
    piece_of_player = None
    current_player = None
    turn = None

    def play_game(self):
        self.current_player = "first"

        self.turn = 0

        board = Board()

        print("start")

        current_player = "first"
        can_move_list = board.get_can_move_list(current_player)
        print(can_move_list)

        current_player = "second"
        can_move_list = board.get_can_move_list(current_player)
        print(can_move_list)

        print("end")

        return 0