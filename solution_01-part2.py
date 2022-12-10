def solution():
    with open("input") as file:
        lines = [line.strip() for line in file]
        

    tmp = 0
    tmpList = []
    for line in lines:
        if line.strip() == "":
            tmp = 0
        else:
            tmp += int(line.strip())
            tmpList.append(tmp)

    tmpList = sorted(tmpList, reverse=True)
    return(sum(tmpList[0:3]))

if __name__ == '__main__':
    print(solution())
