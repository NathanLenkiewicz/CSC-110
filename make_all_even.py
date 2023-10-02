def make_all_even(numbers):
    for i in range(len(numbers)):
        numbers[i] += numbers[i] % 2
    return numbers

def main():
    print(make_all_even([1,2,3,4]))
main()