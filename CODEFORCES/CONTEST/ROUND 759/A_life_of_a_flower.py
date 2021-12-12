def program():
    test_cases = int(input())
    for _ in range(test_cases):
        days_len = int(input())
        sample = input()
        days = [int(day) for day in sample.split(" ")]
        flower_length = 1
        #preconditions
        if days[0] == 1:
            flower_length += 1
        for i in range(1, days_len):
            if days[i-1] == 1 and days[i] == 1:
                flower_length += 5
            elif days[i-1] == 0 and days[i] == 1:
                flower_length += 1
            elif days[i-1] == 0 and days[i] == 0:
                flower_length = -1
                break
        print(flower_length)
    
if __name__ == "__main__":
    program()