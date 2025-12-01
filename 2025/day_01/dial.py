
def rotate_dial(start, direction, distance):
    if direction == 'L':
        return (start - distance) % 100
    elif direction == 'R':
        return (start + distance) % 100
    else:
        raise ValueError("Invalid direction; must be 'L' or 'R'")
