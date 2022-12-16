def read_input():
    with open("input") as file:
        input_lines = [list(line.strip().split(" ")) for line in file]
    return input_lines

def fill_crate(crate, crate_input):
    for char in crate_input:
        crate.append(char)
    return crate

def fill_all_crates(crates):
    fill_crate(crates[0], ["F",
                          "D",
                          "B",
                          "Z",
                          "T",
                          "J",
                          "R",
                          "N"])

    fill_crate(crates[1], ["R",
                          "S",
                          "N",
                          "J",
                          "H"])

    fill_crate(crates[2], ["C",
                          "R",
                          "N",
                          "J",
                          "G",
                          "Z",
                          "F",
                          "Q"])

    fill_crate(crates[3], ["F",
                          "V",
                          "N",
                          "G",
                          "R",
                          "T",
                          "Q"])

    fill_crate(crates[4], ["L",
                          "T",
                          "Q",
                          "F"])

    fill_crate(crates[5], ["Q",
                          "C",
                          "W",
                          "Z",
                          "B",
                          "R",
                          "G",
                          "N"])

    fill_crate(crates[6], ["F",
                          "C",
                          "L",
                          "S",
                          "N",
                          "H",
                          "M"])
    
    fill_crate(crates[7], ["D",
                          "N",
                          "Q",
                          "M",
                          "T",
                          "J"])

    fill_crate(crates[8], ["P",
                          "G",
                          "S"])

def sort_crate(times, crate_from, crate_to):
    for x in range(0, times):
        if crate_from:
            crate_to.append(crate_from.pop())

def solution():
    crates = [[] for x in range(9)]
    sort_orders = read_input()
    fill_all_crates(crates)
    for order in sort_orders:
        sort_crate(int(order[0]), crates[int(order[1]) - 1], crates[int(order[2]) - 1])

    for crate in crates:
        print(crate[len(crate)-1])

if __name__ == '__main__':
    solution()
