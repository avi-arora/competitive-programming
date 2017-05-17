test_cases = int(input())
for _ in range(test_cases):
	dish_one = [dish for dish in input().split(" ")]
	dish_two = [dish for dish in input().split(" ")]
	count = 0
	answer = "dissimilar"
	for dish in dish_one:
		if dish in dish_two:
			count += 1
		if count == 2:
			answer = "similar"
			break
	print(answer)


