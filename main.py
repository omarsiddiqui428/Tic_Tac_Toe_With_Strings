# Tic Tac Toe Program
print("Welcome to Tic Tac Toe")

from helpers import draw_board, check_turn, check_win

spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

playing = True
complete = False
turn = 0
last_turn = -1
while playing: #explain here
    draw_board(spots)
    if last_turn == turn:
        print("That spot is taken, pick an open spot")
    last_turn = turn

    print("Player " + str((turn % 2) + 1) + "'s turn: Pick your spot or press Q to quit" )
    choice = input()
    if choice == 'Q':
        playing = False
    elif choice in ['1','2','3','4','5','6','7','8','9']:
        if spots[int(choice)] not in ["X","O"]:
            turn += 1
            spots[int(choice)] = check_turn(turn)

    if check_win(spots) == True:
        playing = False
        complete = True

    if turn > 8:
        playing = False
        complete = False

draw_board(spots)

if complete == True:
    if check_turn(turn) == "X":
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")

else:
    print("The game is tied. No winner.")

print("Thanks for playing!")

#every single other program requries a main function, so that's why we have this specific syntax
#Add computer player using rand
#Machine learning creates AI. Machine learning is creating a program in a way that it gets better/smarter as the program runs
#Machine learning to make this smarter- know this program inside and out to optimize it with Machine learning