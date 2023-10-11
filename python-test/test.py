def reverse_words(string):
	# split the string into a list of words
	words = string.split()

	# initialize an empty string to store the reversed words
	reversed_string = ''

	# loop through the words in reverse order and append them to the reversed string
	for i in range(len(words)-1, -1, -1):
		reversed_string += words[i] + ' '

	# remove the extra space at the end of the reversed string and return it
	return reversed_string.strip()

# example usage
string = "geeks quiz practice code"
reversed_string = reverse_words(string)
print(reversed_string) # output: "code practice quiz geeks"
