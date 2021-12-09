def program():
    name = input()
    address = input()
    randomString = input()
    #check if name and random string can be made from randomString
    for n in name+address:
        if n in randomString:
            randomString = randomString.replace(n, '',1)
        else:
            print("NO")
            return
    if randomString == "":
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    program()

