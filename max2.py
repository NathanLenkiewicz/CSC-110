def max_of_two(a, b):
    if (a > b):
        return f"{a} is greater than {b}"
    elif (b > a):
        return f"{b} is greater than {a}"
    else:
        return f"{a} is equal to {b}"
    
def main():
    first_num = int(input("First num: "))
    second_num = int(input("Second num: "))

    print(max_of_two(first_num, second_num))

main()