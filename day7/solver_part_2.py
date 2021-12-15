FILE_NAME = 'input.txt'

def solve():
    crab_pos = get_crab_positions()
    crab_pos_freq_map = count_frequency(crab_pos)
    min_pos, max_pos = get_min_and_max(crab_pos)
    crab_pos_cost = get_cost(crab_pos_freq_map, min_pos, max_pos)
    pos_cost_lowest = get_entry_of_lowest_value(crab_pos_cost)
    print(pos_cost_lowest)


def get_crab_positions():
    with open(FILE_NAME) as f:
        crab_pos = [int(x) for x in f.readline().split(',')]
    f.close()
    return crab_pos

def count_frequency(arr):
    d = {}
    for e in arr:
        if not e in d:
            d[e] = 0
        d[e] += 1

    return d

def get_min_and_max(arr):
    min = arr[0]
    max = arr[0]
    for e in arr:
        if e < min:
            min = e
        if e > max:
            max = e

    return (min, max)


def get_cost(pos_freq_map, min_pos, max_pos):
    cost = {}
    for target in range(min_pos, max_pos + 1):
        for to_compare in pos_freq_map:
            if target != to_compare:
                if not target in cost:
                    cost[target] = 0
                pos_diff = abs(to_compare - target)
                cost[target] += (pos_diff * (pos_diff + 1)) / 2 * pos_freq_map.get(to_compare)

    return cost

def get_entry_of_lowest_value(dict):
    lowest_value = None
    for key, value in dict.items():
        if lowest_value == None:
            lowest_value = (key, value)
        else:
            lowest_value = (key, value) if value < lowest_value[1] else lowest_value

    return lowest_value


if __name__ == '__main__':
    solve()