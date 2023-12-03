index_sum = 0

with open('day2/cube_conundrum.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Split the index part and data part
        split_line = line.split(':')
        index_part = split_line[0].strip()
        index = index_part.split(" ")
        data_part = split_line[1].strip()
        data_separated = data_part.split(";")

        # Parse into the list of dictionaries
        sets = []
        for set in data_separated:
            values_raw = set.split(",")
            values_stripped = [value.strip() for value in values_raw]
            color_number = {}
            for item in values_stripped:
                number, color = item.split(maxsplit=1)
                color_number[color] = int(number)
            sets.append(color_number)

        above_threshold = False

        # Specify the threshold values
        thresholds = {'blue': 14, 'red': 12, 'green': 13}

        # Check if above treshold
        for dict in sets:
            if any(color in dict and dict[color] > threshold for color, threshold in thresholds.items()):
                above_threshold = True
                break

        # If not above treshold then add index value to sum of indexes    
        if not above_threshold:
            index_sum += int(index[1])

print(index_sum)