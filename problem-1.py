"""
	PRIME1 - Prime Generator
	#number-theory
	Peter wants to generate some prime numbers for his cryptosystem. 
	Help him! Your task is to generate all prime numbers between two given numbers!

	Input

	The input begins with the number t of test cases in a single line (t<=10). 
	In each of the next t lines there are two numbers m 
	and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

	Output

	For every test case print all prime numbers p such that m <= p <= n,
	 one number per line, test cases separated by an empty line.

	Example

	Input:
	2
	1 10
	3 5

	Output:
	2
	3
	5
	7

	3
	5

@author: Avishek Arora
"""
def BruteForcePrime(n):
	"""Returns True if n is a prime number
	   Applies simple brute-force algorithm.
	   n:	number to check whether prime or not.
	"""
	if n > 1:
		for x in range(n-1, 1, -1):
			if n % x == 0:
				return False
		return True
	else:
		return False
