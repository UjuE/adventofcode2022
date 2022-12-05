import re


def tops_of_stacks_of_crates(column_details):
    the_tops = ""
    for label in column_details.keys():
        the_tops = the_tops + column_details[label][0]
    return the_tops


def apply_moves(column_details, moves):
    for move in moves:
        source_ = move['source']
        source_list = column_details[source_]
        destination_ = move['destination']
        destination_list = column_details[destination_]
        moves_ = move['moves']
        for x in range(moves_):
            k = ""
            while k == "":
                k = source_list.pop(0)
            destination_list.insert(0, k)
    return tops_of_stacks_of_crates(column_details)


def apply_moves_9001(column_details, moves):
    for move in moves:
        source_ = move['source']
        source_list = column_details[source_]
        destination_ = move['destination']
        destination_list = column_details[destination_]
        moves_ = move['moves']
        crates_to_move = source_list[0:moves_]
        column_details[destination_] = crates_to_move + destination_list
        column_details[source_] = source_list[moves_:]

    return tops_of_stacks_of_crates(column_details)


def build_moves(moves_string):
    template = "move (\\d+) from (\\d+) to (\\d+)"
    moves = []
    for move in moves_string.splitlines():
        result = re.search(template, move)
        moves.append({
            "moves": int(result.group(1)),
            "source": result.group(2),
            "destination": result.group(3)
        })
    return moves


def build_column_details(column_string):
    k = list(reversed(column_string.splitlines()))
    labels = k[0].strip().split("   ")
    column_details = {}

    remaining = list(map(lambda row: row.replace("[", "").replace("]", ",").replace("    ", ",").split(","), k[1:]))
    for label in labels:
        label_column = []
        for row in remaining:
            if labels.index(label) < len(row):
                label_column.append(row[labels.index(label)].strip())

        column_details[label.strip()] = list(filter(lambda x: len(x) > 0, list(reversed(label_column))))
    return column_details


def separate_columns_from_moves(input_data, func):
    column_moves = input_data.split("\n\n")
    column = column_moves[0]
    moves = column_moves[1]
    return func(build_column_details(column), build_moves(moves))


def answer_one(input_data):
    return separate_columns_from_moves(input_data, apply_moves)


def answer_two(input_data):
    return separate_columns_from_moves(input_data, apply_moves_9001)


def use_input():
    with open("test_input_data.txt", "r") as input_file:
        input_data = input_file.read()
        print("Answer 1.", answer_one(input_data))
        print("Answer 2.", answer_two(input_data))


use_input()