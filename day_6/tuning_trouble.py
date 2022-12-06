
def index_of_marker(line, marker_length=4):
    for index in range(0, len(line)):
        if len(set(line[index: index+marker_length])) is marker_length:
            return index + marker_length
    return -1


def answer_one(input_data):
    lines_result = []
    for line in input_data.splitlines():
        lines_result.append(index_of_marker(line))
    return lines_result


def answer_two(input_data):
    lines_result = []
    for line in input_data.splitlines():
        lines_result.append(index_of_marker(line, 14))
    return lines_result


def use_input():
    with open("input_data.txt", "r") as input_file:
        input_data = input_file.read()
        print("Answer 1.", answer_one(input_data))
        print("Answer 2.", answer_two(input_data))


use_input()