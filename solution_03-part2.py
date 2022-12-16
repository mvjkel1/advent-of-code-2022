def solution():
    with open("input") as file:
        input_lines = [line.strip() for line in file]

    result = 0
    lowercase = {chr(i + 96) : i for i in range(1, 27)}
    uppercase = {chr(i + 38) : i for i in range(27, 53)}
    lines_counter = 0
    lines_list = []
    for line in input_lines:
        lines_list.append(list(line))
        lines_counter = lines_counter + 1
        if (lines_counter == 3):
            lines_counter = 0
            tmp = [el for el in lines_list[0] if el in lines_list[1]]
            duplicate = [el for el in tmp if el in lines_list[2]][0]
            if (duplicate in lowercase):
                result += lowercase[duplicate]
            else:
                result += uppercase[duplicate]
            lines_list = []
    return result

if __name__ == '__main__':
    print(solution())
