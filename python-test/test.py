# Python program for the above approach

# Function to reverse the words in string
def reverse_word(s, start, end):
	while start < end:
		s[start], s[end] = s[end], s[start]
		start += 1
		end -= 1

# Function to reverse the string
def reverse_string(s):
	s = list(s)
	start, end = 0, len(s) - 1
	reverse_word(s, start, end)

	start = end = 0

	# Iterate over the string S
	while end < len(s):
		if s[end] == ' ':
			reverse_word(s, start, end - 1)
			start = end + 1
		end += 1

	# Reverse the words
	reverse_word(s, start, end - 1)
	return ''.join(s)


# Driver Code
S = "geeks quiz practice code"
print(reverse_string(S))
