#user input
def run():
	test_cases = int(input())
	for test in range(test_cases):
		length = int(input())
		digits = [int(number) for number in input().split()]
		#input completed
		#check for every pair of number,
		i, flag = 0, 0
		while i < length:
			j = 0
			while j < length:
				if j == i:
					j = j + 1
					continue
				else:
					product = digits[i] * digits[j]
					if product not in digits:
						flag = 1
						break
					j = j + 1
			if flag == 1:
				break
			i = i + 1
		if flag == 1:
			print("no")
		else:
			print("yes")
run()

		


