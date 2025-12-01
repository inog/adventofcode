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

def read_parameters_from_file(filename):
    parameters = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                direction = line[0]
                distance = int(line[1:])
                parameters.append((direction, distance))
    return parameters

if __name__ == "__main__":
    file_path = "01-input.csv"
    parameters = read_parameters_from_file(file_path)

    position = START_POSITION
    for direction, value in parameters:
        position = rotate_dial(position, direction, value)

    print(f"Final position of the dial: {position}")
    zero_count = count_0_in_sequence(parameters)
    print(f"Number of times the dial points to 0: {zero_count}")