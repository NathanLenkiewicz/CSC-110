def csv_to_list(file_name):
    numbers = []
    data = open(file_name)
    for i in data:
        list_values = i.strip().split(",")
        if (list_values[1].isnumeric()):
            numbers.append(list_values[1])
    return numbers

def count_start_digits(numbers):
    occurence = {}
    for i in range(len(numbers)):
        integer_i = int(numbers[i][0])
        if (integer_i not in occurence):
            occurence[integer_i] = 1
        else:
            occurence[integer_i] += 1
    return occurence

def calculate_percentages(counts):
    percentages = {}
    sum = 0
    for key, value in counts.items():
        print(value)
        sum += value
    return sum
        

nums = csv_to_list("places.csv")

occurences = count_start_digits(nums)

print(calculate_percentages(occurences))