def rev_sentence(sentence):
    list = sentence.split()
    list.reverse()
    sentence = ' '.join(list)
    return sentence


if __name__ == "__main__":
    input = input("Type a sentence: ")
    print(rev_sentence(input))
