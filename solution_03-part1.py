import string


def solution():
    with open("input") as file:
        lines = [line.strip() for line in file]

    result = 0
    lowercase = {chr(i + 96) : i for i in range(1, 27)}
    uppercase = {chr(i + 38) : i for i in range(27, 53)}

    for line in lines:
        string1 = list(line.strip()[:len(line) // 2])
        string2 = list(line.strip()[len(line) // 2:])
        tmp = [el for el in string1 if el in string2][0]
        if (tmp in lowercase):
            result += lowercase[tmp]
        else:
            result += uppercase[tmp]
    return result


if __name__ == '__main__':
    print(solution())


