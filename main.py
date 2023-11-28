# Tic Tac Toe Program
print("Welcome to Tic Tac Toe")

from helpers import draw_board, check_turn, check_win

spot1 = 1
spot2 = 2
spot3 = 3
spot4 = 4
spot5 = 5
spot6 = 6
spot7 = 7
spot8 = 8
spot9 = 9

playing = True
complete = False
turn = 0
last_turn = -1
while playing: #explain here
    draw_board(spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9)
    if last_turn == turn:
        print("That spot is taken, pick an open spot")
    last_turn = turn

    print("Player " + str((turn % 2) + 1) + "'s turn: Pick your spot or press Q to quit" )
    choice = input()
    if choice == 'Q':
        playing = False
    elif choice in ['1','2','3','4','5','6','7','8','9']:
        current_spot = int(choice)
        spot_value = eval(f'spot{current_spot}')

        if spot_value not in ["X","O"]:
            turn += 1
            exec(f"spot{current_spot} = check_turn(turn)")

    if check_win(spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9) == True:
        playing = False
        complete = True

    if turn > 8:
        playing = False
        complete = False

draw_board(spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9)

if complete == True:
    if check_turn(turn) == "X":
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")

else:
    print("The game is tied. No winner.")

print("Thanks for playing!")
