def main():
	test_cases = int(input())
	for test in range(test_cases):
		x1, y1, x2, y2 = [int(number) for number in input().split()]
		#if x co-ordinate changes
		if y1 == y2 and x1 != x2:
			difference = x2 - x1
			if difference > 0:
				# +ve answer, moving direction is +ve x-axis, which is right
				answer = "right"
			else:
				# -ve answer, moving direction is -ve x-axis, which is left
				answer = "left"
		elif x1 == x2 and y1 != y2:
			difference = y2 - y1
			if difference > 0:
				# +ve answer, moving direction is +ve y-axis, which is up
				answer = "up"
			else:
				# -ve answer, moving direction is -ve y-axis, which is down
				answer = "down"
		else:
			# our robot can't move in both direction simultaneously, lost forever :( )
			answer = "sad"

		print(answer)
main()
