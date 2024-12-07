def main():
    file_path = '01.txt'
    first_values = []
    other_values = []

    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split()
            if columns:
                first_values.append(int(columns[0]))
                other_values.append(int(columns [1]))

    first_values.sort()
    other_values.sort()
    merged_list = list(zip(first_values, other_values))

    print("First values:", first_values)
    print("Other values:", other_values)
    print("Merged list:", merged_list)

    distance = 0
    for first, second in merged_list:
        if first > second:
           distance += (first - second)
        else:
            distance += (second - first)

    print("Distance:", distance)


if __name__ == "__main__":
    main()