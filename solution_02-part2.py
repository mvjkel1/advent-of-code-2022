# A = ROCK (1)
# B = PAPER (2)
# C = SCISSORS (3)

# X = LOSS (1)
# Y = DRAW (2)
# Z = WIN (3)

def solution():
    dict = {
        "A X" : 3,
        "A Y" : 4,
        "A Z" : 8,
        "B X" : 1,
        "B Y" : 5,
        "B Z" : 9,
        "C X" : 2,
        "C Y" : 6,
        "C Z" : 7,
    }

    with open("input") as file:
        lines = [line.strip() for line in file]

    result = 0
    for key in dict:
        result += dict[key] * lines.count(key)
    return result

if __name__ == '__main__':
    print(solution())


