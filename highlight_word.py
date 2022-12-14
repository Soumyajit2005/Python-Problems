# The highlight_word function changes the given word in a sentence to its upper-case version. For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day"

def highlight_word(sentence, word):
	return(sentence[:sentence.index(word)]+ word.upper() + sentence[sentence.index(word)+len(word):])

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))