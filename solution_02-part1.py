# A = ROCK (1)
# B = PAPER (2)
# C = SCISSORS (3)

# X = ROCK (1)
# Y = PAPER (2)
# Z = SCISSORS (3)

def solution():
    dict = {
        "A X" : 4, # rock v rock -> draw = 1 + 3 = 4
        "A Y" : 8, # rock v paper -> win = 2 + 6 = 8
        "A Z" : 3, # rock v scissors -> lose = 3 + 0 = 3
        "B X" : 1, # paper v rock -> lose = 1 + 0 = 1
        "B Y" : 5, # paper v paper -> draw = 2 + 3 = 5
        "B Z" : 9, # paper v scissors -> win = 3 + 6 = 9
        "C X" : 7, # scissors v rock -> win = 1 + 6 = 7
        "C Y" : 2, # scissors v paper -> lose = 2 + 0 = 2
        "C Z" : 6, # scissors v scissors -> draw = 3 + 3 = 6
    }

    with open("input") as file:
        lines = [line.strip() for line in file]

    result = 0
    for key in dict:
        result += dict[key] * lines.count(key)
    return result

if __name__ == '__main__':
    print(solution())


