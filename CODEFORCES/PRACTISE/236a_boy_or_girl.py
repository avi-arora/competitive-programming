
def program():
    s = input()
    distinctString = ""
    for c in s:
        if c not in distinctString:
            distinctString += c
    if len(distinctString) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")



if __name__ == "__main__":
    program()