def detect_duplicates(list_a, list_b):

    for i in range(len(list_a)):
        if list_a[i] in list_b:
            return True
    return False

def main():
    assert detect_duplicates([], []) == False
    assert detect_duplicates(["a", "b"], ["c", "d", "a"]) == True
    assert detect_duplicates([0, 3, 2, 1, 2, 4], [5, 6, 0]) == True
    print("All test cases passed")
main()