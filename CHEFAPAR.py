test_cases = int(input());
for t in range(test_cases):
	total_months = int(input())
	statement = []
	for month in range(total_months):
		statement += [int(input())]
	#input ends.
	total_unpaid_months = 0
	total_unpaid_fine = 0
	CHARGES = 1000
	LATEFINE = 100

	starting_index = 0
	#special handling for starting consecutive one's (1's)
	for i in range(len(statement)):
		if statement[i] == 1:
			starting_index += 1
		else:
			break

	for s in range(starting_index, len(statement)):
		if statement[s] == 0:
			total_unpaid_months += 1
			total_unpaid_fine += 1
		else:
			total_unpaid_fine += 1

	print((total_unpaid_months * CHARGES) + (total_unpaid_fine * LATEFINE))






