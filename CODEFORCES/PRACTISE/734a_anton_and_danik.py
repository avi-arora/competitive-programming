def program():
    test_cases = int(input())
    anton, danik = 0, 0
    string = input()
    for c in string:
        if c == "A":
            anton += 1
        else:
            danik += 1

    if anton > danik:
        print("Anton")
    elif danik > anton:
        print("Danik")
    else: 
        print("Friendship")



if __name__ == "__main__":
    program()