filename = "input.txt"

CONST_FORWARD = "forward"
CONST_UP = "up"
CONST_DOWN = "down"

x = 0
y = 0
with open(filename) as f:
    for line in f:
        direction, unit = line.split(' ')
        if direction == CONST_FORWARD:
            x += int(unit)
        elif direction == CONST_UP:
            y -= int(unit)
        elif direction == CONST_DOWN:
            y += int(unit)
        else:
            raise Exception('Invalid direction')

print(x*y)