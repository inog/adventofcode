START_POSITION = 50


def rotate_dial(start, direction, distance):
    if direction == 'L':
        return (start - distance) % 100
    elif direction == 'R':
        return (start + distance) % 100
    else:
        raise ValueError("Invalid direction; must be 'L' or 'R'")

def count_0_in_sequence(parameters):
    position = START_POSITION
    count_0 = 0
    for direction, value in parameters:
        position = rotate_dial(position, direction, value)
        if position == 0:
            count_0 += 1
    return count_0
