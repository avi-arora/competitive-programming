"""
	Problem description: A positive integer is called a palindrome,
	 if its representation in the decimal system is the same when read from left to right and from right to left. 
	 For a given positive integer K of not more than 1000000 digits, write the value of the smallest palindrome larger than K to output.
	 Numbers are always displayed without leading zeros.

	 Inputs: The first line contains integer t, the number of test cases. Integers K are given in the next t lines.

	 Outputs: For each K, output the smallest palindrome larger than K.

@author: Avishek Arora
"""
def next_palindrome_brute_force(number):
	if number < 9: #for single digit palindrome
		number += 1
		return number 
	else:
		while True:
			number += 1
			if number == int(str(number)[::-1]):
				return number
def improved_palindrome(inputstr):
	characters = []
	for char in inputstr:
		characters += [char]
	center = len(characters) // 2
	first = 0
	last = -1
	if inputstr != inputstr[::-1]: #if number is not palindrome.
		while first < center: #make the number palindrome by mirroring
			if characters[first] != characters[last]:
				characters[last] = characters[first]
			first += 1; last -= 1
	
	#if palindrome is bigger than inputstr, return it
	palindrome = ''.join(characters)
	if palindrome > inputstr:
		return palindrome
	else:
		if len(inputstr) % 2 != 0:
			if characters[center] < '9':
				characters[center] = str(int(characters[center]) + 1)
				return ''.join(characters)
			else:
				characters[center] = '0'
				for c in range(1, center+1):
					if characters[center - c] < '9':
						characters[center - c] = characters[center + c] = str(int(characters[center + c]) + 1)
						return ''.join(characters)
					characters[center - c] = characters[center + c] = '0'
				characters[-1] = '1'
				return '1' + ''.join(characters)
		else:
			if characters[center] < '9' and characters[center - 1] < '9':
				characters[center] = str(int(characters[center]) + 1)
				characters[center-1] = str(int(characters[center-1]) + 1)
				return ''.join(characters)
			else:
				for c in range(0,center+1):
					if characters[center + c] < '9':
						characters[center + c] = characters[center - c - 1] = str(int(characters[center + c]) + 1)
						return ''.join(characters)
					characters[center + c] = characters[center - c - 1] = '0'
					characters[-1] = '1'
				return '1' + ''.join(characters)

def run():
	total_cases = input()
	cases = []
	for x in range(0, total_cases):
		cases += [input()]
	
