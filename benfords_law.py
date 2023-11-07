def csv_to_list(file_name):
    numbers = []
    data = open(file_name)
    for i in data:
        list_values = i.strip().split(",")
        if (len(list_values) > 1):
            if (list_values[len(list_values)-1].isnumeric()):
                numbers.append(list_values[len(list_values)-1])
        elif (len(list_values) <= 1):
            if list_values[0].isnumeric():
                numbers.append(list_values[0])
    return numbers

def count_start_digits(numbers):
    occurence = {}
    for i in range(len(numbers)):
        integer_i = int(numbers[i][0])
        if (integer_i not in occurence and integer_i != 0):
            occurence[integer_i] = 1
        elif (integer_i in occurence and integer_i != 0):
            occurence[integer_i] += 1
    return occurence

def digit_percentages(counts):
    percentages = {}
    sum = 0
    for value in counts.values():
        sum += value
    for key, value in counts.items():
        percentages[key] = round((value / sum) * 100, 2)
    return percentages

def check_benfords_law(percentages):
    percentage_range = {1: 30, 2: 17, 3: 12, 4: 9, 5: 7, 6: 6, 7: 5, 8: 5, 9: 4}
    difference_dict = {}
    follows_benfords_law = True

    for key, value in percentages.items():
        difference_dict[key] = round(value - percentage_range[key], 2)

    for key, value in difference_dict.items():
        if value < 2.5:
            follows_benfords_law = True
        else:
            follows_benfords_law = False

    return follows_benfords_law
