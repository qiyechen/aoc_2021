FILE_NAME = 'input.txt'
BREEDING_CYCLE = 7
NEW_FISH_CYCLE = 9

def solve():
    ages = get_fish_ages()
    age_populations = get_fish_age_to_population_map(ages)
    cycled_populations = cycle(age_populations, 256)
    print(sum(cycled_populations))

def get_fish_ages():
    with open(FILE_NAME) as f:
        ages = [int(x) for x in f.readline().split(',')]
    f.close()
    return ages

def get_fish_age_to_population_map(ages):
    age_populations = [0] * NEW_FISH_CYCLE

    for age in ages:
        age_populations[age] += 1

    return age_populations


def cycle(age_populations, num_day):
    for d in range(num_day):
        new_fishes = age_populations[0]
        cycled_populations = rotate_array_left(age_populations[0:BREEDING_CYCLE])
        cycled_populations[len(cycled_populations) - 1] += age_populations[BREEDING_CYCLE]
        for i in range(BREEDING_CYCLE+1, len(age_populations)):
            cycled_populations.append(age_populations[i])
        cycled_populations.append(new_fishes)
        age_populations = cycled_populations

    return cycled_populations


def rotate_array_left(arr):
    arr_size = len(arr)
    rotated_array = [None] * arr_size

    for i in range(arr_size):
        rotated_array[(i - 1) % arr_size] = arr[i]

    return rotated_array

if __name__ == '__main__':
    solve()