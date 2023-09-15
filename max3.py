def max_of_three(x, y, z):
    if (x > y) and (x > z):
        return x
    elif (y > x) and (y > z):
        return y
    else:
        return z

def main():
    print(max_of_three(4, 2, 3))

main()