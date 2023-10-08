def mean(numbers):
    sum = 0
    number_of_nums = 0
    index = 0
    
    if (len(numbers) > 0):
        while (index < len(numbers)):
            sum += numbers[index]
            number_of_nums += 1
            index += 1
    else:
        return 0
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

def sd(numbers):
    
    variance_1 = variance(numbers)
    return round((variance_1)**0.5, 2)

def list_range(numbers):
    if (len(numbers) > 0):
        index_max = 0
        index_min = 0
        max_value = numbers[0]
        min_value = numbers[0]
            # find max value
        while (index_max < len(numbers)):
            if (numbers[index_max] > max_value):
                max_value = numbers[index_max]
            index_max += 1
        
        while (index_min < len(numbers)):
            if numbers[index_min] < min_value:
                min_value = numbers[index_min]
            index_min += 1
    else:
        return 0

    return max_value - min_value


def main():
  value = mean([])
  assert value == 0, \
      f"expected return value was 0, but function returned {value}" 
  
  value = mean([0, 0, 0])
  assert value == 0, \
      f"expected return value was 0, but function returned {value}" 
  
  value = mean([4, 5, 2])
  assert value == 3.67, \
      f"expected return value was 3.67, but function returned {value}" 
  
  value = variance([4, 5, 2])
  assert value == 2.33, \
      f"expected return value was 2.33, but function returned {value}" 
       
  value = sd([4, 5, 2])
  assert value == 1.53, \
      f"expected return value was 1.53, but function returned {value}"
  
  value = list_range([4, 5, 2])
  assert value == 3, \
      f"expected return value was 3, but function returned {value}"
  
  value = list_range([])
  assert value == 0, \
      f"expected return value was 0, but function returned {value}"

  print("All tests passed.")


main()


