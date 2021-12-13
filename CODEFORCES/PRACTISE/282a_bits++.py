def program():
    total_statements = int(input())
    x = 0
    for _ in range(total_statements):
        statement = input()
        if(statement[0] == "+" or statement[1] == "+"):
            x+=1
        else:
            x-=1
    return x




if __name__ == "__main__":
    print(program())