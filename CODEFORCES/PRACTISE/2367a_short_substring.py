def program():
    test_cases = int(input())
    for _ in range(test_cases):
        b = input()
        if len(b) == 2:
            print(b)
        else:
            a = b[0]
            for i in range(1,len(b),2):
                a += b[i]
            print(a)




if __name__ == "__main__":
    program()