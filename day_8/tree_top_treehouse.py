
def is_edge(x, y, max_column_index, max_row_index):
    return x == 0 or x == max_row_index or y == 0 or y == max_column_index


def scenic_score_in_x_path(x, y, grid):
    row = grid[x]
    value = row[y]
    left_trees = list(reversed(row[0:y]))
    right_trees = row[y+1:]
    left_visible_trees = 0
    right_visible_trees = 0

    for left_tree in left_trees:
        left_visible_trees = left_visible_trees + 1
        if left_tree >= value:
            break

    for right_tree in right_trees:
        right_visible_trees = right_visible_trees + 1
        if right_tree >= value:
            break

    return left_visible_trees * right_visible_trees


def scenic_score_in_y_path(x, y, grid):
    value = grid[x][y]
    top_trees = list(reversed(list(map(lambda row: row[y], grid[0:x]))))
    bottom_trees = list((map(lambda row: row[y], grid[x+1:])))

    top_visible_trees = 0
    bottom_visible_trees = 0

    for top_tree in top_trees:
        top_visible_trees = top_visible_trees + 1
        if top_tree >= value:
            break

    for bottom_tree in bottom_trees:
        bottom_visible_trees = bottom_visible_trees + 1
        if bottom_tree >= value:
            break

    return top_visible_trees * bottom_visible_trees


def is_hidden_in_x_path(x, y, grid, max_row_index):
    row = grid[x]
    value = row[y]
    hidden_from_left = False
    hidden_from_right = False
    # compute hidden from the left
    for left_index in range(y):
        if row[left_index] >= value:
            hidden_from_left = True
    for right_index in range(y+1, max_row_index +1):
        if row[right_index] >= value:
            hidden_from_right = True

    return hidden_from_left and hidden_from_right


def is_hidden_in_y_path(x, y, grid, max_column_index):
    value = grid[x][y]
    hidden_from_top = False
    hidden_from_bottom = False

    for top_index in range(x):
        if grid[top_index][y] >= value:
            hidden_from_top = True
    for bottom_index in range(x+ 1, max_column_index+1):
        if grid[bottom_index][y] >= value:
            hidden_from_bottom = True
    return hidden_from_bottom and hidden_from_top


def answer_one(input_data):
    data_lines = input_data.splitlines()
    max_column_index = len(data_lines) - 1
    max_row_length = len(data_lines[0]) - 1
    the_grid = list(map(lambda row: list(map(lambda strnumber: int(strnumber), list(row))), data_lines))
    count = 0

    for y in range(max_column_index + 1):
        for x in range(max_row_length + 1):
            is_visible = is_edge(x, y, max_column_index, max_row_length) \
                        or not is_hidden_in_x_path(x, y, the_grid, max_row_length) \
                        or not is_hidden_in_y_path(x, y, the_grid, max_column_index)

            if is_visible:
                count = count + 1
    return count


def answer_two(input_data):
    data_lines = input_data.splitlines()
    max_column_index = len(data_lines) - 1
    max_row_length = len(data_lines[0]) - 1
    the_grid = list(map(lambda row: list(map(lambda strnumber: int(strnumber), list(row))), data_lines))

    max_score = 0
    for y in range(max_column_index + 1):
        for x in range(max_row_length + 1):
            scenic_score = scenic_score_in_y_path(x, y, the_grid) * \
                           scenic_score_in_x_path(x, y, the_grid)
            if scenic_score > max_score:
                max_score = scenic_score

    return max_score


def use_input():
    with open("input_data.txt", "r") as input_file:
        input_data = input_file.read()
        print("Answer 1.", answer_one(input_data))
        print("Answer 2.", answer_two(input_data))


use_input()