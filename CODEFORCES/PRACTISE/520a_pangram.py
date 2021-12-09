import string

def program():
    no_of_char = int(input())
    input_string = input()
    alphabet = string.ascii_lowercase
    for c in range(no_of_char):
        if input_string[c].lower() in alphabet:
            alphabet = alphabet.replace(input_string[c].lower(), '')
    if alphabet == "":
        print("YES")
    else:
        print("NO")


        



if __name__ == "__main__":
    program()