

def string_to_list(input_data: str) -> list:
    list_of_elves = []
    for elf_data in input_data.split("\n\n"):
        elf_data = list(filter(lambda x: x and x.strip(), elf_data.splitlines()))
        list_of_elves.append(list(map(lambda y: int(y), elf_data)))
    return list_of_elves


def highest_calorie_total(list_of_elves: list) -> list:
    k = list(map(lambda elf_data: sum(elf_data), list_of_elves))
    return sorted(k, reverse=True)


def use_input():
    with open("test_input_data.txt", "r") as input_file:
        input_data = input_file.read()
        most_calories = highest_calorie_total(string_to_list(input_data))
        print("answer 1", sum(most_calories[0:1]))
        print("answer 2", sum(most_calories[0:3]))


use_input()