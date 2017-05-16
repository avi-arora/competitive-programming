test_cases = int(input())
for _ in range(test_cases):
	str = input()
	found, ans = 0, 0
	end = 0
	for c in str:
		if c == '1' and found == 0:
			found = 1
		elif c == '1' and found == 1 and end == 1:
			ans = "NO"
			break
		elif c != '1' and found == 1:
			end = 1
	if found == 1 and ans == 0:
		ans = "YES"
	else:
		ans = "NO"
	print(ans)