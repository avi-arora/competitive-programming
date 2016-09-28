"""
	Problem description: A positive integer is called a palindrome, if its representation in the decimal system is the same when read from left to right and from right to left. For a given positive integer K of not more than 1000000 digits, write the value of the smallest palindrome larger than K to output.
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
	#if number is not palindrome, make it palindrome by mirroring.
	palindrome = left = middle = right = ''
	center = len(inputstr) // 2
	if inputstr != inputstr[::-1]:
		if center % 2 != 0: # for even number
			left = inputstr[:center-1]
			middle = inputstr[center - 1] + inputstr[::-1][center:center + 1]
			right = inputstr[::-1][center + 1:]
		else: 
			left = inputstr[:center]
			middle = inputstr[center]
			right = inputstr[::-1][center + 1:]
	else:
		if center % 2 != 0:
			left = inputstr[:center - 1]
			middle = inputstr[center -1] + inputstr[center:center + 1]
			right = inputstr[center+1:]
		else:
			left = inputstr[:center]
			middle = inputstr[center]
			right = inputstr[center + 1:]
	palindrome = left + middle + right
	if palindrome > inputstr:
		return palindrome
	if center % 2 != 0:
		if middle[0] < '9':
			middle = str(int(middle[0]) + 1) * 2
			palindrome = left + middle + right
			return palindrome
		else:
			pass
	else:
		if middle < '9':
			middle = str(int(middle) + 1)
			palindrome = left + middle + right
			return palindrome
		else:
			pass

def run():
	total_cases = input()
	for _ in range(total_cases):
		improved_palindrome(raw_input())
	
