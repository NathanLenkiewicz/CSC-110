def every_two_together(characters):

    even_indicies = ""

    for i in range(0, len(characters), 2):
        even_indicies += characters[i]


    return even_indicies

def main():
    print(every_two_together(["a", "e", "p", "o", "p", "w", "l", "i", "e", "f"]))

main()