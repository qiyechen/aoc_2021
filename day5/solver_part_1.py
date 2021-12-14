FILE_NAME = 'input.txt'

def solve():
    start_coordinates, end_coordinates, largest_x, largest_y = get_report()
    map = [[0 for y in range(largest_y + 1)] for x in range(largest_x + 1)]
    solve_directions(start_coordinates, end_coordinates, map)
    print(get_num_of_danger_areas(map))

def get_report():
    with open(FILE_NAME) as f:

        start_coordinates = []
        end_coordinates = []
        largest_x = 0
        largest_y = 0
        for line in f:
            x1, y1, x2, y2 = [int(value) for value in line.strip().replace(' -> ', ',').split(',')]
            start_coordinates.append((x1, y1))
            end_coordinates.append((x2, y2))
            largest_x = max(largest_x, x1, x2)
            largest_y = max(largest_y ,y1, y2)
    f.close()

    return start_coordinates, end_coordinates, largest_x, largest_y

def solve_directions(start_coordinates, end_coordinates, map):
    num_coordinates = len(start_coordinates)

    for i in range(num_coordinates):
        start_coordinate = start_coordinates[i]
        end_coordinate = end_coordinates[i]
        if start_coordinate[1] ==  end_coordinate[1]:       # horizontal
            y = start_coordinate[1]
            step = 1 if start_coordinate[0] < end_coordinate[0] else -1
            for x in range(start_coordinate[0], end_coordinate[0] + step, step):
                map[x][y] += 1
        elif start_coordinate[0] == end_coordinate[0]:      # vertical
            x = start_coordinate[0]
            step = 1 if start_coordinate[1] <  end_coordinate[1] else -1
            for y in range(start_coordinate[1], end_coordinate[1] + step, step):
                map[x][y] += 1
        else:
            print("diagonal, ignore...")

def get_num_of_danger_areas(map):
    num_of_danger_areas = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] >= 2:
                num_of_danger_areas += 1
    return num_of_danger_areas

if __name__ == '__main__':
    solve()