#!/usr/bin/env python3

def swap(st):
	vowels = 'aeiou'
	new_word = ''
	for letter in st:
		if letter in vowels:
			new_word += letter.capitalize()
			continue
		new_word += letter
	return new_word


print(swap('victor vinicius reis de matos'))
