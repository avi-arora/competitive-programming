test_cases = int(input())
for test in range(test_cases):
	number = int(input())
	total_trailing_zeros = 0
	x = 1
	while True:
		result = int(number / (5 ** x))
		if result <= 0:
			break
		total_trailing_zeros += result
		x += 1

	print(total_trailing_zeros)
