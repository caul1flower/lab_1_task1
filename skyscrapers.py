"""
Module for the game 'Skyscrapers'.
Reads file check.txt and returns if the combination
on the board is winning or not.

GitHub: https://github.com/caul1flower/lab_1_task1
"""

def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.
    """
    board = []
    with open(path, 'r') as input_file:
        for line in input_file:
            board.append(*line.split())
    return board


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    counter = 0
    previous_elem = 0
    for element in input_line[1:-1]:
        if element == '?':
            return False
        element = int(element)
        if element > previous_elem:
            counter += 1
            previous_elem = element

    if counter == pivot:
        return True
    return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board[1:-1]:
        for element in line:
            if element == '?':
                return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board[1:-1]:
        line = set(line[1:-1])
        if '*' in line and len(set(line)) == 6:
            return True
        elif len(set(line)) != 5:
            return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board[1:-1]:
        if line[0] == '*' and line[-1] != '*':
            line = ''.join(reversed(line))

        elif line[0] != '*' and line[-1] != '*':
            if not left_to_right_check(line, int(line[0])):
                return False
            line = ''.join(reversed(line))

        elif line[0] == line[-1] == '*':
            continue

        if not left_to_right_check(line, int(line[0])):
            return False

    return True


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    new_board = []
    for symbol in range(len(board)):
        new_line = []
        for line in board:
            new_line += line[symbol]
        new_line = ''.join(new_line)
        new_board.append(new_line)
    return (check_uniqueness_in_rows(new_board) and
            check_horizontal_visibility(new_board))


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """
    board = read_input(input_path)

    if (not check_not_finished_board(board) or not
        check_uniqueness_in_rows(board) or not
        check_horizontal_visibility(board) or not check_columns(board)):
        return False

    return True

if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))