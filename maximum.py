def maximum(*numbers):
    if (len(numbers) > 0):
        max_value = numbers[0]
        for i in range(len(numbers)):
            if numbers[i] >= max_value:
                max_value = numbers[i]
        return max_value, 2
    
print(maximum(1,2,3))
