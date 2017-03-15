test_cases = int(input());
for t in range(test_cases):
	total_months = int(input())
	statement = list(map(int, input().split()))
	#input ends.

	CHARGES = 1000
	LATEFINE = 100

	#remove the consecutive 1's untill 0 is encountered
	first_zero = 0
	for s in statement:
		if s == 0:
			break
		first_zero += 1

	statement = statement[first_zero:] 

	#count the number of one's
	total_one = 0
	for s in statement:
		if s == 1:
			total_one += 1

	print((len(statement) * 1100) - (total_one * CHARGES))




