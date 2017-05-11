#user input
test_cases = int(input())
for test in range(test_cases):
	length = int(input())
	digits = [int(number) for number in input().split()]
	#input completed
	flag = 0
	for i in range(len(digits) - 1):
		product = digits[i] * digits[i+1];
		if product in digits:
			flag = 1
			break
	if flag == 1:
		print("yes")
	else:
		print("no")


