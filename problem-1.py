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
from math import sqrt

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

def SieveOfEratosthenes(n):
	"""Returns list of Primes between 2 to n
	   Take advantage of sieve of eratosthenes algorithm
	   n:	upper bound starting from 2 to n
	"""
	n += 1
	numbers = [True] * n
	for i in range(0,int(sqrt(n))):
			if numbers[i] == True:
					for j in range((i+2)**2,n,(i+2)): #Using Formulae for crossing non-primes i.e i^2, i^2+i, i^2+2i, ... n
							numbers[j-2] = False #j-2 because starting memory from 0, hence saving two blocks of memeory locations.
	primes = [i+2 for i in range(0,n-2) if numbers[i] == True]
	return primes 

def SegmentedSOE(start, end):
	"""Prints list of Primes between start to end
	   Uses Segmented sieve algorithm
	   start: lower bound >= 1, 
	   end:   upper bound <= 10^9
	   TC: O(n log log n),
	   SC: sqrt(n)
	"""
	#Get the primes till sqrt(end) using SOE
	segment_size = int(sqrt(end))
	primes = SieveOfEratosthenes(segment_size)
	#print the obvious primes if falls into range
	if start <= segment_size:
		for prime in primes:
			if prime >= start:
				print prime
	#remove 2 in prime's list as we are sieving upon odds numerals
	#no factors of 2 is to be found by sieving odds numbers
	primes.remove(2)
	if start < segment_size:
	 	start = primes[-1] + 2 if (primes[-1] + 1) % 2 == 0 else primes[-1] + 1
	elif start % 2 == 0:
		start += 1	
	segment = range(start, start + ((segment_size * 2) - 1), 2) # Initilize the first segment
	stop = True # tell's when to stop the algorithm, not to compute redundant prime's exceeds range
	while stop:
		start = segment[-1] + 2
		for prime in primes:
			composite = (segment[0] // prime) * prime 
			composite = composite + prime if composite < segment[0] else composite 
			for i in range(composite, composite + ((segment_size * 2) - 1), prime):
				if i in segment:
					segment.remove(i)
		#what's left in segment are prime's, print and update
		for p in segment:
			if p > end:
				stop = False 
				break
			print p
		segment = range(start, start + ((segment_size * 2) - 1), 2)
	print # for new line
def run():
		testcases = input()
		assert testcases <= 10, "No: of test cases must be <= 10"
		inputs = []
		for i in range(0,testcases):
			m , n = map(int, raw_input().split())
			assert all([ m >= 1, n >= m, n <= 1000000000, n - m <= 100000 ]), "Test Case Error."
			inputs += [[m, n]]
		for i in inputs:
			SegmentedSOE(i[0], i[1])
run()
		