test_cases = int(input())
for _ in range(test_cases):
	turn, winner, value = 0, 0, 1
	max_limak, max_bob = [int(value) for value in input().split()]
	while True:
		if turn == 0:
			# This represents as Limak's turn
			if value <= max_limak:
				max_limak -= value
				value += 1
				turn = 1 # represent next turn, which is of bob
				continue
			else:
				winner = 1
				break
		if turn == 1:
			# This represents as Bob's turn
			if value <= max_bob:
				max_bob -= value
				value += 1
				turn = 0 # now next turn is of limak
				continue
			else:
				winner = 0
				break
	if winner == 0:
		print("Limak")
	else:
		print("Bob")

