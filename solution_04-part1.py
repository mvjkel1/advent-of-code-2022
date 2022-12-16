import re

def solution():
    with open("input") as file:
        input_lines = [line.strip() for line in file]

    counter = 0
    for line in input_lines:
        numbers = re.search("([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)", line)
        first_list = [int(numbers.group(1)), int(numbers.group(2))]
        second_list = [int(numbers.group(3)), int(numbers.group(4))]
        if (first_list[0] == second_list[0] and first_list[1] == second_list[1]) \
            or (first_list[0] >= second_list[0] and first_list[1] <= second_list[1]) \
            or (first_list[0] <= second_list[0] and first_list[1] > second_list[1]) \
            or ((first_list[0] == first_list[1]) and (first_list[1] >= second_list[0] and first_list[1] <= second_list[1])) \
            or ((second_list[0] == second_list[1]) and (second_list[1] >= first_list[0] and second_list[1] <= first_list[1])):
            print(first_list, second_list)
            counter = counter + 1
    return counter

if __name__ == '__main__':
    print(solution())
