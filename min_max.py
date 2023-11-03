def min_max(*values):
    if (len(values) > 0):
        min_value = values[0]
        max_value = values[0]
        for i in values:
            if i >= max_value:
                max_value = i
            else:
                min_value = i
        return min_value, max_value
    
print(min_max(2,4,6))