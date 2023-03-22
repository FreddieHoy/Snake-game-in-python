bytes = [128, 64, 32, 16, 8, 4, 2, 1]


def doConvert(number: int):
    machineCode = []
    total = 0

    for b in bytes:
        if total == number:
            machineCode.append(0)

        elif number >= b + total:
            total += b
            machineCode.append(1)

        else:
            machineCode.append(0)

    return machineCode
    # return an array of 8 o's or 1's
