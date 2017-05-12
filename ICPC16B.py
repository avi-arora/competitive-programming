#user input
def main():
	test_cases = int(input())
	for test in range(test_cases):
		length = int(input())
		digits = [int(number) for number in input().split()]
		#input completed
		#check for every pair of number,
		print(isBeautiful(digits))
		
def isBeautiful(input):
	""" Return yes if input array is bueautiful, else returns no
		Instead of checking for every single pairs, we make assumptions regarding the values, which is true
		We're trying to find one case in which the condition does not hold a[k] = a[i] * a[j],

	    Time Complexity: O(n), Linear time
	    Space Complexity: (1), Constant
	"""

	ones, minusones, others = 0, 0, 0
	for digit in input:
		if digit == 0:
			continue
		elif digit == 1:
			ones = ones + 1
		elif digit == -1:
			minusones = minusones + 1
		else:
			others = others + 1
			if others > 1:
				return 'no'

	if others == 1 and minusones > 0:
		return 'no'
	elif minusones > 1 and ones == 0:
		return 'no'

	return 'yes'

main()	
