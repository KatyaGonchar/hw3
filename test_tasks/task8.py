def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(5):
        if all([board[row][col] == player for row in range(5)]):
            return True

    if all([board[i][i] == player for i in range(5)]):
        return True

    if all([board[i][4 - i] == player for i in range(5)]):
        return True

    return False


def check_draw(board):
    return all(board[row][col] != ' ' for row in range(5) for col in range(5))


def is_valid_move(board, row, col):
    return 0 <= row < 5 and 0 <= col < 5 and board[row][col] == ' '


def game():
    board = [[' ' for _ in range(5)] for _ in range(5)]
    players = ['X', 'O']
    turn = 0

    while True:
        for row in board:
            print(row)

        player = players[turn % 2]
        print(f"Player {player}, your turn!")

        try:
            row, col = map(int, input("Enter row and column (fo example, 1 1): ").split())
            row -= 1
            col -= 1
        except ValueError:
            print("Wrong values.")
            continue

        if not is_valid_move(board, row, col):
            print("Wrong move. Try again.")
            continue

        board[row][col] = player

        if check_winner(board, player):
            for row in board:
                print(row)
            print(f"The player {player} won!")
            break

        if check_draw(board):
            for row in board:
                print(row)
            print("Draw!")
            break

        turn += 1


game()
