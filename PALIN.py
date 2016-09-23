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
def imporved_palindrome(inputstr):
	characters = []
	for char in inputstr:
		characters += [char]
	stop = len(characters) // 2
	first = 0
	last = -1
	if inputstr != inputstr[::-1]: #if number is not palindrome.
		while first < stop: #make the number palindrome by mirroring
			if characters[first] != characters[last]:
				characters[last] = characters[first]
			first += 1; last -= 1
	
	#if palindrome is bigger than inputstr, return it
	palindrome = ''.join(characters)
	if palindrome > inputstr:
		return palindrome
	else:
		return 0
		
		

	
def run():
	total_cases = input()
	cases = []
	for x in range(0, total_cases):
		cases += [input()]
	