
def convert(str):
    stack, i = [], 0
    output = ""
    while i < len(str):
        if not isOperator(str[i]):
            output += str[i]
            i+=1
        else:
            if str[i] == "(":
                stack.append(str[i])
                i+=1
            elif str[i] == ")":
                while (len(stack) > 0 and stack[len(stack)-1] != "("):
                    output += stack.pop()
                if(len(stack) > 0 and stack[len(stack)-1] == "("):
                    stack.pop()
                i+=1
            else:
                #operator encountered
                if (len(stack) > 0 and getPriority(str[i]) > getPriority(stack[len(stack)-1])) or (len(stack) > 0 and stack[len(stack)-1] == "("): 
                    stack.append(str[i])
                    i+=1
                else:
                    while len(stack) > 0 and getPriority(str[i]) <= getPriority(stack[len(stack)-1]) and stack[len(stack)-1] != '(':
                        output += stack.pop()
                    stack.append(str[i])
                    i+=1
        
         
    while len(stack) != 0:
        output+=stack.pop()
    return output
            
    
def isOperator(c):
    if c == "+" or c == "-" or c =="^" or c=="$" or c=="/" or c=="*" or c==")" or c== "(":
        return True
    else:
         return False
    


def getPriority(c):
    if c=="(" or c==")":
        return 4
    elif c=="$" or c=="^":
        return 3
    elif c=="*" or c=="/":
        return 2
    elif c=="+" or c=="-":
        return 1

if __name__ == "__main__":
    user_input = input()
    print(convert(user_input))

    