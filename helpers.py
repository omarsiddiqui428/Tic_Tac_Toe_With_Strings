def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)


def check_turn(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"


def check_win(spots):
    if (spots[1] == spots[2] == spots[3]
            or spots[4] == spots[5] == spots[6]
            or spots[7] == spots[8] == spots[9]
            or spots[1] == spots[4] == spots[7]
            or spots[2] == spots[5] == spots[8]
            or spots[3] == spots[6] == spots[9]
            or spots[7] == spots[5] == spots[3]
            or spots[1] == spots[5] == spots[9]):
        return True

    # if (spots[1] in ["X", "O"]
    #         and spots[2] in ["X", "O"]
    #         and spots[3] in ["X", "O"]
    #         and spots[4] in ["X", "O"]
    #         and spots[5] in ["X", "O"]
    #         and spots[6] in ["X", "O"]
    #         and spots[7] in ["X", "O"]
    #         and spots[8] in ["X", "O"]
    #         and spots[8] in ["X", "O"]):
    #     return True
    else:
        return False
