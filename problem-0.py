"""
	TEST - Life, the Universe, and Everything
	#basic #tutorial

	Your program is to use the brute-force approach in order to find the Answer 
	to Life, the Universe, and Everything.
	More precisely... rewrite small numbers from input to output. 
	Stop processing input after reading in the number 42.
	All numbers at input are integers of one or two digits.

	@author- Avishek Arora
"""
num = 0
while True:
	num = input()
	if num == 42:
		break
	print(num)
