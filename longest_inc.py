def run():
	#take input
	size = int(input())
	input_list = []
	for i in range(size):
		input_list.append(int(input()))
	#input completed

	print(LISLengthDP(input_list))




def LISLengthBruteForce():
	test_cases = int(input())
	input_list = []
	for t in range(test_cases):
		input_list.append(int(input()))

	all_length = []
	for number in input_list:
		last = number
		sub = [last]
		for n in input_list[input_list.index(last):]:
			if n > last:
				sub.append(n)
				last = n
		all_length.append(len(sub))
	return max(all_length)


def LISLengthRecursive(sequence, previous, current):
	""" Computes the length of the longest increasing subsequence
	    time complexity: O(2^n)
	    space complexity: O(1)

	    >>> LISLengthRecursive([4,3,1,5,2,6,9,12,8,15], 0, 0)
	    6
	    >>> LISLengthRecursive([10,9,2,5,3,7,101,18], 0, 0)
	    4
	    >>> LISLengthRecursive([2,7,4,3,8], 0, 0)
	    3
	"""
	if current == len(sequence):
		return 0;

	taken, not_taken = 0, 0
	if sequence[current] > previous:
		taken = 1 + LISLengthRecursive(sequence, sequence[current], current+1)
	not_taken = LISLengthRecursive(sequence, previous, current+1)

	return max(taken, not_taken)

def LISLengthDP(sequence):
	""" Computes the length of the longest increasing subsequence
	    time complexity: O(n^2)
	    space complexity: O(n)

	    >>> LISLengthDP([4,3,1,5,2,6,9,12,8,15])
	    6
	    >>> LISLengthDP([10,9,2,5,3,7,101,18])
	    4
	    >>> LISLengthDP([2,7,4,3,8])
	    3
	"""
	dp = [1] * len(sequence)
	j = 1
	while j < len(sequence):
		i = 0
		while i < j:
			if sequence[j] > sequence[i]:
				if dp[j] < dp[i] + 1:
					dp[j] = dp[i] + 1
			i = i + 1
		j = j + 1
	return max(dp)
run()
#adding doctest
if __name__ == "__main__":
	import doctest
	doctest.testmod()

	