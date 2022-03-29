
def infixToPrefix(str):
    #reverse the string with taken care of parenthesis
    str, i = str[::-1], 0
    inputStr = ""
    while i < len(str):
        if str[i] == "(":
            inputStr += ")"
        elif str[i] == ")":
            inputStr += "("
        else:
            inputStr += str[i]
        i+=1
    #compute postfix
    postFix = infixToPostfix(inputStr)
    return postFix[::-1]
    

def infixToPostfix(str):
    stack, i = [], 0
    output = ""
    while i < len(str):
        if not isOperator(str[i]):
            output+=str[i]
            i+=1
        else:
            #check for )
            if str[i] == "(":
                stack.append(str[i])
                i+=1
            elif str[i] == ")":
                while len(stack) > 0 and stack[len(stack)-1] != "(":
                    output += stack.pop()
                if len(stack) > 0 and stack[len(stack)-1] == "(":
                    stack.pop()
                i+=1
            else:
                #if str[i] is operator
                if (len(stack) > 0 and getOperatorPriority(str[i]) > getOperatorPriority(stack[len(stack)-1])) or (len(stack) > 0 and stack[len(stack)-1] =="("):
                    stack.append(str[i])
                    i+=1
                else:
                    while len(stack) > 0 and getOperatorPriority(str[i]) <= getOperatorPriority(stack[len(stack)-1]) and stack[len(stack)-1] != "(":
                        output += stack.pop()
                    stack.append(str[i])
                    i+=1
    while len(stack) > 0:
        output += stack.pop()
    return output


def isOperator(c):
    if c == "+" or c=="-" or c=="*" or c=="/" or c=="^" or c=="$" or c=="(" or c==")":
        return True
    else:
        return False

def getOperatorPriority(operator):
    if operator == "+" or operator == "-":
        return 1
    elif operator == "*" or operator == "/":
        return 2
    elif operator == "^" or operator == "$": 
        return 3
    else:
        return 0

if __name__ == "__main__":
    str = input()
  #  print(infixToPostfix(str))
    print(infixToPrefix(str))