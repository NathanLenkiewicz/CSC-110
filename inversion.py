def invert_dictionary(dictionary):
    inverted_dict = {}
    for key, value in dictionary.items():
        # check if the current value is not in the inverted dictionary
        if value not in inverted_dict:
            # check the edge case of the value being an empty string
            if (type(value) == str and len(value) < 1):
                inverted_dict[key] = [value]
            # if the type of value is not a string, continue swapping keys and values
            elif type(value) != str:
                if value not in inverted_dict:
                    inverted_dict[value] = [key]
        # if the current value is in the inverted dictionary, add the key to the 
        # list that corresponds with the current value
        elif value in inverted_dict:
                inverted_dict[value].append(key)

    return inverted_dict
print(invert_dictionary({"a":2, "b": 2}))