def swap_case(s):
    new_string = ""
    for letter in s:
        if letter.isalpha():
            if letter.islower():
                new_string += letter.upper()
            elif letter.isupper():
                new_string += letter.lower()
        else:
            new_string += letter
    return new_string

if __name__ == '__main__':
    s = input("Type a sentence: ")
    result = swap_case(s)
    print(result)