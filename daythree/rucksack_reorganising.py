import string

priority_order = string.ascii_lowercase + string.ascii_uppercase


def priority_of(character):
    return priority_order.index(character) + 1


def check_rucksack_compartments(rucksack_contents):
    half_point_index = int(len(rucksack_contents)/2)
    first_compartment = rucksack_contents[0:half_point_index]
    second_compartment = rucksack_contents[half_point_index: len(rucksack_contents)]

    return set(list(first_compartment)) & (set(list(second_compartment)))


def check_group_similarities(three_elves_rucksacks):
    return set(three_elves_rucksacks[0]) & set(three_elves_rucksacks[1]) & set(three_elves_rucksacks[2])


def elf_groups_from(ruck_sacks):
    chunk_size = 3
    return [ruck_sacks.splitlines()[i:i + chunk_size] for i in range(0, len(ruck_sacks.splitlines()), chunk_size)]


def total_similarities_priorities(similarities):
    return sum(map(lambda x: priority_of(x),  similarities))


def total_of_all_rucksacks(ruck_sacks):
    return sum(map(lambda line: total_similarities_priorities(check_rucksack_compartments(line)),
                   ruck_sacks.splitlines()))


def total_of_all_groups(elf_groups):
    similarities = list(map(lambda group: check_group_similarities(group).pop(), elf_groups))
    return total_similarities_priorities(similarities)


def use_input():
    with open("input_data.txt", "r") as input_file:
        input_data = input_file.read()
        print("Answer 1.", total_of_all_rucksacks(input_data))
        print("Answer 2.", total_of_all_groups(elf_groups_from(input_data)))


use_input()