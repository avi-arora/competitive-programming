

def postfixToInfix(postfix):
    #read the string for left to right
    i, stack = 0, []
    while i < len(postfix):
        if not isOperator(postfix[i]):
            stack.append(postfix[i])
            i+=1
        else:
            # symbol is operator
            str = "(" + stack.pop() + postfix[i] + stack.pop() + ")"
            stack.append(str)
            i+=1
    return stack.pop()


def isOperator(symbol):
    if symbol == "+" or symbol == "-" or symbol == "*" or symbol == "/" or symbol == "^" or symbol == "(" or symbol == ")":
        return True
    else: 
        return False



if __name__ == "__main__":
    str = input()
    print(postfixToInfix(str))