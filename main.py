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


def main():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    show_board(board)

    cell = ask_cell(board)
    board[cell] = "X"
    show_board(board)


main()