def indicies_of_vowels(string):
    indicies = []
    for i in range(len(string)):
        if (string[i] in "aeiouAEIOU"):
            indicies.append(i)
    return indicies

def main():
    print(indicies_of_vowels("hello"))
    print(indicies_of_vowels("aeiou"))
    print(indicies_of_vowels(""))
        
main()