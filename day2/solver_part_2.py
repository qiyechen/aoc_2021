filename = 'input.txt'

CONST_FORWARD = 'forward'
CONST_UP = 'up'
CONST_DOWN = 'down'

x = 0
y = 0
aim = 0
with open(filename) as f:
    for line in f:
        direction, unit = line.split(' ')
        if direction == CONST_FORWARD:
            x += int(unit)
            y += aim * int(unit)
        elif direction == CONST_UP:
            aim -= int(unit)
        elif direction == CONST_DOWN:
            aim += int(unit)
        else:
            raise Exception("Invalid direction.")
f.close()
print(x*y)