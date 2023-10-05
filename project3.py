def mean(numbers):
    sum = 0
    number_of_nums = 0
    index = 0

    while (index < len(numbers)):
        sum += numbers[index]
        number_of_nums += 1
        index += 1
    return round((sum / number_of_nums), 2)

def variance(numbers):
    # calculate variance by finding the mean
    # of the list numbers, summing the squares
    # of the difference between each value in
    # numbers and the mean * in the formula x is
    # each value in numbers
    index = 0
    mean_value = mean(numbers)
    total = 0

    while (index < len(numbers)):
        total += (numbers[index] - mean_value)**2
        index += 1
    return round((total / (len(numbers)-1)), 2)

print(variance([4,5,2]))