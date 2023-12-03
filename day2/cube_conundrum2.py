sum_of_products = 0

with open('day2/cube_conundrum.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # # Split the index part and data part
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

        # Create a dictionary to store the highest values for each color
        highest_values = {}

        # Iterate through the list of dictionaries
        for dict in sets:
            # Update the highest values dictionary for each color
            for color, value in dict.items():
                highest_values[color] = max(highest_values.get(color, 0), value)

        # Multipli the highest values
        product = 1
        for value in highest_values.values():
            product *= value
        
        # Add the multiplied highest values
        sum_of_products += product
        
print(sum_of_products)