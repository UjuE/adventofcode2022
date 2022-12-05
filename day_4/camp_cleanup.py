def the_range(the_range_string):
    v = []
    k = the_range_string.split("-")

    for n in range(int(k[0]), int(k[1])+1):
        v.append(n)

    return set(v)


def is_intersect(elf_group_details):
    intersect = elf_group_details[0].intersection(elf_group_details[1])
    return len(intersect) > 0


def is_subset(elf_group_details):
    return elf_group_details[0].issubset(elf_group_details[1]) or elf_group_details[1].issubset(elf_group_details[0])


def parse_elf_group(elf_group_details_string: str, func):
    split = elf_group_details_string.split(",")
    elf_group_details = list(map(the_range, split))
    return func(elf_group_details)


def answer_one(input_data):
    count = 0
    for parse_line in input_data.splitlines():
        it_contains = parse_elf_group(parse_line, is_subset)
        if it_contains:
            count = count + 1
    return count


def answer_two(input_data):
    count = 0
    for parse_line in input_data.splitlines():
        it_contains = parse_elf_group(parse_line, is_intersect)
        if it_contains:
            count = count + 1
    return count


def use_input():
    with open("input_data.txt", "r") as input_file:
        input_data = input_file.read()
        print("Answer 1.", answer_one(input_data))
        print("Answer 2.", answer_two(input_data))


use_input()