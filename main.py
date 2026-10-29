WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def show_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


def ask_cell(board):
    while True:
        text = input("Номер клетки (1-9): ")

        if not text.isdecimal():
            print("Нужно ввести число от 1 до 9")
            continue

        number = int(text)

        if number < 1 or number > 9:
            print("Такой клетки нет, введите число от 1 до 9")
            continue

        if board[number - 1] in ("X", "O"):
            print("Эта клетка уже занята, выберите другую")
            continue

        return number - 1


def check_win(board, player):
    for a, b, c in WIN_LINES:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False


def play():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    player = "X"

    for _ in range(9):
        show_board(board)
        print("Ходит", player)

        cell = ask_cell(board)
        board[cell] = player

        if check_win(board, player):
            show_board(board)
            print("Победил", player)
            return

        if player == "X":
            player = "O"
        else:
            player = "X"

    show_board(board)
    print("Ничья")


while True:
    play()
    answer = input("Сыграть ещё раз? (да/нет): ")
    if answer.lower() != "да":
        break