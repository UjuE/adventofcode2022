
class Crt:
    def __init__(self):
        self.monitor_pixels = [['⬛'] * 40] * 6

    # def log_
    def process(self, cycle, register):
        row = int(cycle / 40)
        column = cycle % 40
        if (cycle -1) % 40 in (register - 1, register + 2):
                self.monitor_pixels[row][column] = '⬜'

    def print_monitor(self):
        for row in self.monitor_pixels:
            print(''.join(row))

Crt().print_monitor()

def i_just_dive_in(input_data, func = ()):
    commands = {
        "noop": lambda x, y: print("do nothing"),
        "addx": lambda x, add: x + add
    }

    x = 1
    xs = [x]
    cycle_count = 0
    last_command = None
    last_function = None
    signal_strength = []
    cycles_x = []
    for line in input_data.splitlines():

        for detail in line.split(" "):
            if cycle_count in [20, 60, 100, 140, 180, 220]:
                print("Boosting", cycle_count, x, cycle_count * x)
                signal_strength.append(cycle_count * x)

            if last_function is not None:
                x = last_function
            cycle_count = cycle_count + 1
            func(cycle_count, x)
            if detail in commands.keys():
                last_command = detail
                last_function = x
            else:
                value = int(detail)
                xs.append(value)
                last_function = commands[last_command](x, value)
                last_command = None

    return sum(signal_strength)


def answer_one(input_data):
    return i_just_dive_in(input_data)


def answer_two(input_data):
    crt = Crt()
    i_just_dive_in(input_data, crt.process)
    crt.print_monitor()
    pass


def use_input():
    with open("input_data.txt", "r") as input_file:
        input_data = input_file.read()
        # print("Answer 1.", answer_one(input_data))
        print("Answer 2.", answer_two(input_data))


use_input()