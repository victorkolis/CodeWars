# Link: https://www.codewars.com/kata/5831c204a31721e2ae000294/train/python
#
# Description:
# When provided with a String, capitalize all vowels
# For example:
# Input : "Hello World!"
# Output : "HEllO WOrld!"
# Note: Y is not a vowel in this kata.


def swap(st):
	vowels = 'aeiou'
	new_word = ''
	for letter in st:
		if letter in vowels:
			new_word += letter.capitalize()
			continue
		new_word += letter
	return new_word


print(swap('victor kolis'))

# maketrans
# translate