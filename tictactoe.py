"""משחק איקס-עיגול לשני שחקנים."""


BOARD_SIZE = 3
EMPTY = " "


def create_board():
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board(board):
    print()
    print("    1   2   3")
    print("  +---+---+---+")
    for i, row in enumerate(board):
        cells = " | ".join(row)
        print(f"{i + 1} | {cells} |")
        print("  +---+---+---+")
    print()


def is_valid_move(board, row, col):
    return (
        0 <= row < BOARD_SIZE
        and 0 <= col < BOARD_SIZE
        and board[row][col] == EMPTY
    )


def make_move(board, row, col, player):
    board[row][col] = player


def check_winner(board):
    lines = []

    # שורות ועמודות
    for i in range(BOARD_SIZE):
        lines.append(board[i])
        lines.append([board[0][i], board[1][i], board[2][i]])

    # אלכסונים
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line[0] != EMPTY and line[0] == line[1] == line[2]:
            return line[0]
    return None


def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)


def get_move(player):
    while True:
        raw = input(f"שחקן {player}, בחר שורה ועמודה (לדוגמה: 1 2): ").strip()
        parts = raw.split()
        if len(parts) != 2:
            print("קלט לא תקין. הזן שני מספרים מופרדים ברווח.")
            continue
        try:
            row = int(parts[0]) - 1
            col = int(parts[1]) - 1
        except ValueError:
            print("יש להזין מספרים בלבד.")
            continue
        return row, col


def play_game():
    board = create_board()
    current = "X"

    print("=" * 32)
    print("       משחק איקס-עיגול")
    print("=" * 32)
    print("שחקן X מתחיל. הזן שורה ואז עמודה.")

    while True:
        print_board(board)
        row, col = get_move(current)

        if not is_valid_move(board, row, col):
            print("מהלך לא חוקי — התא תפוס או מחוץ ללוח. נסה שוב.")
            continue

        make_move(board, row, col, current)

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"שחקן {winner} ניצח! 🎉")
            return

        if is_board_full(board):
            print_board(board)
            print("תיקו!")
            return

        current = "O" if current == "X" else "X"


def main():
    while True:
        play_game()
        again = input("לשחק שוב? (כ/ל): ").strip()
        if again not in ("כ", "כן", "y", "Y", "yes"):
            print("להתראות!")
            break


if __name__ == "__main__":
    main()
