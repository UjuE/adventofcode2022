

def string_to_list(input_data: str) -> list:
    list_of_elves = []
    for elf_data in input_data.split("\n\n"):
        elf_data = list(filter(lambda x: x and x.strip(), elf_data.splitlines()))
        list_of_elves.append(list(map(lambda y: int(y), elf_data)))
    return list_of_elves


def highest_calorie_total(list_of_elves: list) -> list:
    k = list(map(lambda elf_data: sum(elf_data), list_of_elves))
    return sorted(k, reverse=True)


def sum_it(calorie_totals, count):
    total = 0
    for index in range(0, count):
        total += calorie_totals[index]

    return total


def use_input():
    with open("test_input_data.txt", "r") as input_file:
        input_data = input_file.read()
        most_calories = highest_calorie_total(string_to_list(input_data))
        print("answer 1", sum_it(most_calories, 1))
        print("answer 2", sum_it(most_calories, 3))


use_input()