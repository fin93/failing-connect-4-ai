board_cols = 7
board_rows = 6
player_o = "o"
player_x = "x"
board = [
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "x", "x", "x", "-", "-"]
]


def print_board(boar):
    for i in range(board_rows):
        for j in range(board_cols):
            print(boar[i][j], end=" ")
        print()


def is_col_full(boar, col):
    for i in range(board_rows):
        if boar[i][col] == "-":
            return False
    return True


def is_whole_full(boar):
    for i in range(board_rows):
        for j in range(board_cols):
            if boar[i][j] == "-":
                return False
    return True


def mark(boar, col, active_player):
    for i in range(board_rows):
        if boar[5][col] == "-":
            boar[5][col] = active_player
            break
        elif boar[i][col] != "-" and not is_col_full(boar, col):
            boar[i - 1][col] = active_player
            break


def has_won(boar, active):
    for i in range(board_rows):
        for j in range(board_cols):
            if boar[i][j - 3] == boar[i][j - 2] and boar[i][j - 3] == boar[i][j - 1]:
                if boar[i][j - 3] == boar[i][j] and boar[i][j - 3] == active:
                    return True
            if boar[i - 3][j] == boar[i - 2][j] and boar[i - 3][j] == boar[i - 1][j]:
                if boar[i - 3][j] == boar[i][j] and boar[i - 3][j] == active:
                    return True
            if boar[i - 3][j - 3] == boar[i - 2][j - 2] and boar[i - 3][j - 3] == boar[i - 1][j - 1]:
                if boar[i - 3][j - 3] == boar[i][j] and boar[i - 3][j - 3] == active:
                    return True
            if boar[5 - i][j - 3] == boar[4 - i][j - 2] and boar[5 - i][j - 3] == boar[3 - i][j - 1]:
                if boar[5 - i][j - 3] == boar[2 - i][j] and boar[5 - i][j - 3] == active:
                    return True
    return False


def cases(boar):
    for i in range(board_rows):
        for j in range(board_cols):
            if j > 2:
                if boar[i][j - 3] == boar[i][j - 2] and boar[i][j - 3] == boar[i][j - 1]:
                    if boar[i][j - 3] == player_x and boar[i][j] == "-":
                        if i == 5:
                            mark(boar, j, player_o)
                        if i < 5:
                            if boar[i + 1][j] != "-":
                                mark(boar, j, player_o)
                        return True
                if boar[i][j - 3] == boar[i][j - 2] and boar[i][j - 1] == "-":
                    if boar[i][j - 3] == boar[i][j] and boar[i][j - 3] == player_x:
                        if i == 5:
                            mark(boar, j - 1, player_o)
                        if i < 5:
                            if boar[i + 1][j] != "-":
                                mark(boar, j - 1, player_o)
                        return True
                if boar[i][j - 2] == "-" and boar[i][j - 3] == boar[i][j - 1]:
                    if boar[i][j - 3] == boar[i][j] and boar[i][j - 3] == player_x:
                        if i == 5:
                            mark(boar, j - 2, player_o)
                        if i < 5:
                            if boar[i + 1][j] != "-":
                                mark(boar, j - 2, player_o)
                        return True
                if boar[i][j - 3] == "-" and boar[i][j - 2] == boar[i][j - 1]:
                    if boar[i][j - 2] == boar[i][j] and boar[i][j - 2] == player_x:
                        if i == 5:
                            mark(boar, j - 3, player_o)
                        if i < 5:
                            if boar[i + 1][j] != "-":
                                mark(boar, j - 3, player_o)
                        return True
            if i > 2:
                if boar[i - 3][j] == boar[i - 2][j] and boar[i - 3][j] == boar[i - 1][j]:
                    if boar[i - 3][j] == player_x and boar[i][j] == "-":
                        mark(boar, j, player_o)
                        return True

            if boar[i - 3][j - 3] == boar[i - 2][j - 2] and boar[i - 3][j - 3] == boar[i - 1][j - 1]:
                if boar[i - 3][j - 3] == player_x and boar[i][j] == "-":
                    if i == 5:
                        mark(boar, j, player_o)
                    if i < 5:
                        if boar[i + 1][j] != "-":
                            mark(boar, j, player_o)
                    return True
            if boar[i - 3][j - 3] == boar[i - 2][j - 2] and boar[i - 1][j - 1] == "_":
                if boar[i - 3][j - 3] == boar[i][j] and boar[i - 3][j - 3] == player_x:
                    if i == 5:
                        mark(boar, j - 1, player_o)
                    if i < 5:
                        if boar[i + 1][j] != "-":
                            mark(boar, j - 1, player_o)
                    return True
            if boar[i - 2][j - 2] == "-" and boar[i - 3][j - 3] == boar[i - 1][j - 1]:
                if boar[i - 3][j - 3] == boar[i][j] and boar[i - 3][j - 3] == player_x:
                    if i == 5:
                        mark(boar, j - 2, player_o)
                    if i < 5:
                        if boar[i + 1][j] != "-":
                            mark(boar, j - 2, player_o)
                    return True
            if boar[i - 3][j - 3] == "-" and boar[i - 2][j - 2] == boar[i - 1][j - 1]:
                if boar[i - 2][j - 2] == boar[i][j] and boar[i - 2][j - 2] == player_x:
                    if i == 5:
                        mark(boar, j - 3, player_o)
                    if i < 5:
                        if boar[i + 1][j] != "-":
                            mark(boar, j - 3, player_o)
                    return True
            if boar[5 - i][j - 3] == boar[4 - i][j - 2] and boar[5 - i][j - 3] == boar[3 - i][j - 1]:
                if boar[5 - i][j - 3] == player_x and boar[2 - i][j] == "-":
                    if boar[3 - i][j] != "-":
                        mark(boar, j, player_o)
                        return True
    return False




def main():
    active = player_x
    for i in range(board_rows):
        for j in range(board_cols):
            board[i][j] = "-"

    while True:
        """if active == player_x:
            mark(board, int(input("Enter a column[1-7]: ")) - 1, player_x)
            cases(board)
            print_board(board)
            if has_won(board, active):
                break
            active = player_o
        elif active == player_o:
            mark(board, int(input("Enter a column[1-7]: ")) - 1, player_o)
            cases(board)
            print_board(board)
            if has_won(board, active):
                break
            active = player_x
    print(f"{active} has won!")"""
        if has_won(board, player_x):
            break
        mark(board, int(input("Enter a column[1-7]: ")) - 1, player_x)
        cases(board)
        print_board(board)

    if input("Do you want to play again [y/n]: ").lower() == "y":
        main()


if __name__ == '__main__':
    main()
