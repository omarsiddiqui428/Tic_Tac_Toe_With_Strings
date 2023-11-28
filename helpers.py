def draw_board(spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9):
    board = (f"|{spot1}|{spot2}|{spot3}|\n"
             f"|{spot4}|{spot5}|{spot6}|\n"
             f"|{spot7}|{spot8}|{spot9}|")
    print(board)


def check_turn(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"


def check_win(spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9):
    if (spot1 == spot2 == spot3
            or spot4 == spot5 == spot6
            or spot7 == spot8 == spot9
            or spot1 == spot4 == spot7
            or spot2 == spot5 == spot8
            or spot3 == spot6 == spot9
            or spot7 == spot5 == spot3
            or spot1 == spot5 == spot9):
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
