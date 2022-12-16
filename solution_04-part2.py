import re
import itertools as it

def check_overleap(first_list, second_list):
    for first in range(first_list[0], first_list[1] + 1):
        for second in range(second_list[0], second_list[1] + 1):
            if (first == second):
                return 1
    return 0

def solution():
    with open("input") as file:
        input_lines = [line.strip() for line in file]

    counter = 0
    for line in input_lines:
        numbers = re.search("([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)", line)
        first_list = [int(numbers.group(1)), int(numbers.group(2))]
        second_list = [int(numbers.group(3)), int(numbers.group(4))]
        counter = counter + check_overleap(first_list, second_list)
    return counter

if __name__ == '__main__':
    print(solution())
