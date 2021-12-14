FILE_NAME = 'input.txt'

def solve():
    ages = getFishAges()
    cycle(ages, 80)
    print(len(ages))

def getFishAges():
    with open(FILE_NAME) as f:
        ages = [int(x) for x in f.readline().split(',')]
    f.close()
    return ages

def cycle(ages, num_day):
    for d in range(num_day):
        num_fish = len(ages)
        for f in range(num_fish):
            if (ages[f] > 6):
                ages[f] = ages[f] - 1
            else:
                ages[f] = (ages[f] - 1) % 7
                if ages[f] == 6:
                    ages.append(8)

    return ages


if __name__ == '__main__':
    solve()