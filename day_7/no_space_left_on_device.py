import re


class DirectorySystem:
    def __init__(self, name: str):
        self.directory_name = name
        self.files_size = 0
        self.files_sizes = []
        self.parent = None
        self.has_been_listed = False

    def add_size(self, size: int):
        self.files_size = self.files_size + size
        self.files_sizes.append(size)
        if self.parent is not None:
            self.parent.add_size(size)

    def add_parent(self, filesystem):
        self.parent = filesystem

    def first_parent(self):
        return self.parent

    def listing_directory(self):
        self.has_been_listed = True

    def __str__(self):
        return f"<directory_name: {self.directory_name}, " \
               f"files_size: {self.files_size}," \
               f"has_been_listed: {self.has_been_listed}, " \
               f"files_sizes: {self.files_sizes}>"

    def __repr__(self):
        return self.__str__()



def handle_change_directory(line, current_parent_directory, parents_map):
    new_directory = re.compile(r"\$ cd (.*)").search(line).group(1)
    if new_directory == "..":
        current_parent_directory = current_parent_directory.first_parent()
    elif current_parent_directory is None:
        current_parent_directory = DirectorySystem(new_directory)
        parents_map.append(current_parent_directory)
    elif len(list(filter(lambda d: d.directory_name is new_directory, parents_map))) == 1:
        k = list(filter(lambda d: d.directory_name == new_directory, parents_map))
        current_parent_directory = k[0]
    else:
        new_directory_fil = DirectorySystem(new_directory)
        new_directory_fil.add_parent(current_parent_directory)
        current_parent_directory = new_directory_fil
        parents_map.append(current_parent_directory)
    return current_parent_directory, parents_map


def handle_file_list(line, current_parent_directory, parents_map):
    child_directory = re.compile(r"dir (.*)").search(line)
    file_size = re.compile(r"(\d+) .*").search(line)

    if child_directory:
        the_chile_directory = DirectorySystem(child_directory.group(1))
        the_chile_directory.add_parent(current_parent_directory)
        parents_map.append(the_chile_directory)
    else:
        k = int(file_size.group(1))
        current_parent_directory.add_size(k)
    return current_parent_directory, parents_map


def is_changing_directory(line: str):
    return line.startswith("$ cd")


def is_listing_files(line: str):
    return line.startswith("$ ls")


def is_command(line: str):
    return line.startswith("$")


def handle_input(input: str):
    is_listing = False
    current_parent_directory = None
    parents_map = []
    for line in input.splitlines():
        if is_listing and is_changing_directory(line):
            is_listing = False
            current_parent_directory.listing_directory()

        if is_changing_directory(line):
            current_parent_directory, parents_map = handle_change_directory(line,
                                                                            current_parent_directory,
                                                                            parents_map)
        elif is_listing_files(line):
            is_listing = True

        elif is_listing and not current_parent_directory.has_been_listed:
            current_parent_directory, parents_map = handle_file_list(
                line,current_parent_directory, parents_map
            )

    return parents_map


def answer_one(input_data):
    return sum(filter(lambda k: k <= 100000, list(map(lambda v: v.files_size, handle_input(input_data)))))


def answer_two(input_data):
    total_space = 70000000
    desired_freespace = 30000000
    use_space = handle_input(input_data)[0].files_size
    actual_free_space = total_space - use_space
    space_needed = desired_freespace - actual_free_space
    k = list(map(lambda y: y.files_size, list(filter(lambda v: v.files_size >= space_needed, handle_input(input_data)))))
    k.sort()
    return k[0]


def use_input():
    with open("input_data.txt", "r") as input_file:
        input_data = input_file.read()
        print("Answer 1.", answer_one(input_data))
        print("Answer 2.", answer_two(input_data))


use_input()