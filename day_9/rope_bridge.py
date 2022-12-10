import re


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_one_space_different(self, other):
        is_on_x_axis = (self.y == other.y) and abs(self.x - other.x) == 1
        is_on_y_axis = (self.x == other.x) and abs(self.y - other.y) == 1
        is_diagonal = abs(self.x - other.x) == 1 and abs(self.y - other.y) == 1
        return is_on_x_axis or is_on_y_axis or is_diagonal

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def move_tail_on_x(head_position, next_position, is_right_move = True):
    tail_next_step = 1
    if not is_right_move:
        tail_next_step = -1
    if head_position.__eq__(next_position) or head_position.is_one_space_different(next_position):
        return next_position
    elif abs(head_position.x - next_position.x) == 2 and abs(head_position.y - next_position.y) == 1:
        return Position(head_position.x + tail_next_step, head_position.y)
    elif abs(head_position.x - next_position.x) == 2 and head_position.y == next_position.y:
        return Position(next_position.x + tail_next_step, next_position.y)
    else:
        print("ON X","What could possibly be else", head_position, next_position, is_right_move)
        return next_position


def move_tail_on_y(head_position, next_position, is_up_move = True):
    tail_next_step = -1
    if not is_up_move:
        tail_next_step = 1

    if head_position.__eq__(next_position) or head_position.is_one_space_different(next_position):
        return next_position
    elif abs(head_position.y - next_position.y) == 2 and abs(head_position.x - next_position.x) == 1:
        print("\tBut why")
        return Position(head_position.x, head_position.y + tail_next_step)
    elif abs(head_position.x - next_position.x) == 2 and abs(head_position.y - next_position.y) == 1:
        return Position(head_position.x, next_position.y)
    elif abs(head_position.x - next_position.x) > 1 and head_position.y == next_position.y:
        return Position(next_position.x , next_position.y + tail_next_step)
    else:
        print("ON Y","What could possibly be else", head_position, next_position, is_up_move)
        return next_position


def move_rope_up(rope, distance):
    print("Moving Up")
    print(rope)
    last_head_y_position = rope[0][0].y + distance

    while rope[0][0].y <= last_head_y_position:
        last_head = rope[0][0]
        rope[0].insert(0, Position(last_head.x, last_head.y + 1))
        for next_knot in range(1, len(rope)):
            rope[next_knot].insert(0, move_tail_on_y(rope[next_knot - 1][0], rope[next_knot][0], True))
            print("\t", rope)
        print(rope)
    return rope


def move_rope_down(rope, distance):
    last_head_y_position = rope[0][0].y - distance

    while rope[0][0].y >= last_head_y_position:
        last_head = rope[0][0]
        rope[0].insert(0, Position(last_head.x, last_head.y - 1))
        for next_knot in range(1, len(rope)):
            rope[next_knot].insert(0, move_tail_on_y(rope[next_knot - 1][0], rope[next_knot][0], False))

    return rope

def move_rope_left(rope, distance):
    print("Moving left")
    last_head_x_position = rope[0][0].x - distance
    while rope[0][0].x >= last_head_x_position:
        last_head = rope[0][0]
        rope[0].insert(0, Position(last_head.x - 1, last_head.y))
        for next_knot in range(1, len(rope)):
            rope[next_knot].insert(0, move_tail_on_x(rope[next_knot - 1][0], rope[next_knot][0], False))

    return rope

def move_rope_right(rope, distance):
    print("Moving right")
    print(rope)
    last_head_x_position = rope[0][0].x + distance
    while rope[0][0].x < last_head_x_position:
        last_head = rope[0][0]
        rope[0].insert(0, Position(last_head.x + 1, last_head.y))
        for next_knot in range(1, len(rope)):
            rope[next_knot].insert(0, move_tail_on_x(rope[next_knot - 1][0], rope[next_knot][0]))
        print(rope)
    return rope

def move_right(head_position, tail_position, distance, move_head = True):
    print("Right")
    last_head_x_position = head_position.x + distance
    head_positions = [head_position]
    tail_positions = [tail_position]

    while head_positions[0].x < last_head_x_position:
        last_head = head_positions[0]
        next_head = last_head
        if move_head:
            next_head = Position(last_head.x + 1, last_head.y)
            head_positions.insert(0, next_head)
        last_tail = tail_positions[0]
        if last_tail.__eq__(next_head) or last_tail.is_one_space_different(next_head):
            tail_positions.insert(0, last_tail)
        elif next_head.x - last_tail.x == 1 and last_tail.y - next_head.y == 1:
            tail_positions.insert(0, last_tail)
        elif next_head.y == last_tail.y and next_head.x - last_tail.x == 2:
            next_tail = Position(last_tail.x + 1, last_tail.y)
            tail_positions.insert(0, next_tail)
        elif next_head.x - last_tail.x == 2 and next_head.y - last_tail.y == 1:
            next_tail = Position(next_head.x - 1, next_head.y)
            tail_positions.insert(0, next_tail)
        elif last_tail.x == next_head.x or last_tail.x - last_head.x == 1:
            tail_positions.insert(0, last_tail)

        elif next_head.x - last_tail.x == 1 and next_head.y - last_tail.y == 1:
            next_tail = Position(last_tail.x, last_tail.y + 1)
            tail_positions.insert(0, next_tail)

        elif next_head.x - last_tail.x == 2 and last_tail.y - next_head.y == 1:
            next_tail = Position(next_head.x - 1, next_head.y)
            tail_positions.insert(0, next_tail)
        else:
            print("else right",next_head, last_tail)

    return head_positions, tail_positions


def move_up(head_position, tail_position, distance):
    print("Up")
    last_head_y_position = head_position.y + distance
    head_positions = [head_position]
    tail_positions = [tail_position]

    while head_positions[0].y < last_head_y_position:
        last_head = head_positions[0]
        next_head = Position(last_head.x, last_head.y + 1)
        head_positions.insert(0, next_head)
        last_tail = tail_positions[0]
        if last_tail.__eq__(next_head) or last_tail.is_one_space_different(next_head):
            tail_positions.insert(0, last_tail)

        elif last_tail.x - next_head.x == 1 and next_head.y == last_tail.y:
            tail_positions.insert(0, last_tail)
        elif next_head.x - last_tail.x == -1 and next_head.y - last_tail.y == 1:
            tail_positions.insert(0, last_tail)
        elif next_head.x - last_tail.x == -1 and next_head.y - last_tail.y == 1:
            tail_positions.insert(0, last_tail)
        elif next_head.x == last_tail.x:
            next_tail = Position(last_tail.x, last_tail.y+1)
            tail_positions.insert(0, next_tail)
        elif next_head.x - last_tail.x == 1 and next_head.y - last_tail.y == 2:
            next_tail = Position(last_head.x, last_tail.y + 1)
            tail_positions.insert(0, next_tail)
        elif next_head.x - last_tail.x == 1 and next_head.y - last_tail.y == 1:
            tail_positions.insert(0, last_tail)
        elif (last_tail.x == next_head.x and (-1 >= (next_head.y - last_tail.y) <= 1)) or (last_tail.y == next_head.y and (-1 >= (last_tail.x - next_head.x) <= 1)):
            tail_positions.insert(0, last_tail)
        elif next_head.y - last_tail.y == 2:
            next_tail = Position(next_head.x, next_head.y - 1)
            tail_positions.insert(0, next_tail)
        else:
            print("else up",next_head, last_tail)

    return head_positions, tail_positions


def move_left(head_position, tail_position, distance):
    print("Left")
    last_head_x_position = head_position.x - distance
    head_positions = [head_position]
    tail_positions = [tail_position]

    while head_positions[0].x != last_head_x_position:
        last_head = head_positions[0]
        next_head = Position(last_head.x - 1, last_head.y)
        head_positions.insert(0, next_head)
        last_tail = tail_positions[0]

        if last_tail.__eq__(next_head) or last_tail.is_one_space_different(next_head):
            tail_positions.insert(0, last_tail)
        elif last_tail.x - next_head.x == 2 and last_tail.y - next_head.y == 1:
            next_tail = last_head
            tail_positions.insert(0, next_tail)
        elif last_tail.x - next_head.x == 1 and last_tail.y - next_head.y == 1:
            tail_positions.insert(0, last_tail)
        elif next_head.x - last_tail.x == 1 and next_head.y == last_tail.y:
            tail_positions.insert(0, last_tail)
        elif next_head.y == last_tail.y and last_tail.x - next_head.x == 2:
            next_tail = Position(last_tail.x - 1, last_tail.y)
            tail_positions.insert(0, next_tail)
        elif last_tail.x - next_head.x == 1 and next_head.y - last_tail.y == 1:
            tail_positions.insert(0, last_tail)
        elif last_tail.x - next_head.x == 2 and next_head.y - last_tail.y == 1:
            next_tail = Position(last_tail.x - 1, last_tail.y + 1)
            tail_positions.insert(0, next_tail)
        elif (last_tail.x == next_head.x and (-1 >= (next_head.y - last_tail.y) <= 1)) or (last_tail.y == next_head.y and (-1 >= (last_tail.x - next_head.x) <= 1)):
            tail_positions.insert(0, last_tail)
        else:
            print("else left", next_head, last_tail)

    return head_positions, tail_positions


def move_down(head_position, tail_position, distance):
    print("DOWN")
    last_head_y_position = head_position.y - distance
    head_positions = [head_position]
    tail_positions = [tail_position]

    while head_positions[0].y != last_head_y_position:
        last_head = head_positions[0]
        next_head = Position(last_head.x, last_head.y - 1)

        head_positions.insert(0, next_head)
        last_tail = tail_positions[0]

        if last_tail.__eq__(next_head) or last_tail.is_one_space_different(next_head):
            tail_positions.insert(0, last_tail)
        elif next_head.x - last_tail.x == -1 and last_tail.y - next_head.y == 1:
            tail_positions.insert(0, last_tail)
        elif next_head.x - last_tail.x == 1 and next_head.y - last_tail.y == -1:
            tail_positions.insert(0, last_tail)
        elif next_head.x == last_tail.x and last_tail.y - next_head.y == 2:
            next_tail = Position(last_tail.x, last_tail.y - 1)
            tail_positions.insert(0, next_tail)
        elif last_tail.y - next_head.y == 2:
            next_tail = Position(next_head.x, next_head.y + 1)
            tail_positions.insert(0, next_tail)
        elif last_tail.x == next_head.x and last_tail.y - next_head.y == 1:
            tail_positions.insert(0, last_tail)
        else:
            print("else down", next_head, last_tail)

    return head_positions, tail_positions


def just_thinking(line, head_position, tail_position):
    head_movement_map = {
        "R": lambda the_head_position, the_tail_position, the_distance: move_right(the_head_position, the_tail_position, the_distance),
        "U": lambda the_head_position, the_tail_position, the_distance: move_up(the_head_position, the_tail_position, the_distance),
        "L": lambda the_head_position, the_tail_position, the_distance: move_left(the_head_position, the_tail_position, the_distance),
        "D": lambda the_head_position, the_tail_position, the_distance: move_down(the_head_position, the_tail_position, the_distance)
    }
    movement_pattern = re.compile(r"([RULD]) (\d+)")
    movement = movement_pattern.search(line)
    direction = movement.group(1)
    steps = int(movement.group(2))
    head_positions, tail_positions = head_movement_map[direction](head_position, tail_position, steps)

    return head_positions[0], tail_positions[0], tail_positions


def just_thinking_why(line, rope):
    head_movement_map = {
        "R": lambda the_rope, the_distance: move_rope_right(the_rope, the_distance),
        "U": lambda the_rope, the_distance: move_rope_up(the_rope, the_distance),
        "L": lambda the_rope, the_distance: move_rope_left(the_rope, the_distance),
        "D": lambda the_rope, the_distance: move_rope_down(the_rope, the_distance)
    }
    movement_pattern = re.compile(r"([RULD]) (\d+)")
    movement = movement_pattern.search(line)
    direction = movement.group(1)
    steps = int(movement.group(2))
    rope = head_movement_map[direction](rope, steps)

    return rope


def answer_one(input_data):

    head_position = Position(0,0)
    tail_position = Position(0,0)
    tail_positions = [tail_position]
    # grid[x][y] = "HT"
    for line in input_data.splitlines():
        head_position, tail_position, new_tail_positions = just_thinking(line, head_position, tail_position)
        tail_positions.extend(new_tail_positions)

    return len(set(tail_positions))



def answer_two(input_data):
    rope = [[Position(0,0)],[Position(0,0)],[Position(0,0)],[Position(0,0)],[Position(0,0)],[Position(0,0)],[Position(0,0)],[Position(0,0)],[Position(0,0)],[Position(0,0)]]
    for line in input_data.splitlines():
        rope = just_thinking_why(line, rope)

    return len(set(rope[9]))


def use_input():
    with open("input_data.txt", "r") as input_file:
        input_data = input_file.read()
        # print("Answer 1.", answer_one(input_data))
        print("Answer 2.", answer_two(input_data))


use_input()