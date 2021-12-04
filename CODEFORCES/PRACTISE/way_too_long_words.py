def program():
    totalCases = int(input())
    for _ in range(totalCases):
        input_string = input()
        print(shortString(input_string))


def shortString(string):
    return string[0] + str(len(string)-2) + string[len(string)-1]if len(string) > 10 else string

if __name__ == "__main__":
    program()