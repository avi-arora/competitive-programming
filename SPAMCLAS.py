#####################################
# SPAMCLAS: CODECHEF
#####################################

def Compute(minX, maxX, neurons):
    total_user_ids = (maxX - minX) + 1
    NOT_SPAM, SPAM = total_user_ids // 2, total_user_ids // 2
    if total_user_ids % 2 == 1: #no of userids have odd parity
        if minX % 2 != 0: #starting userid is even
            SPAM += 1
        else:
            NOT_SPAM += 1
    for (weight, bias) in neurons:
        if bias % 2 != 0: #bias is odd
            if weight % 2 != 0:
                NOT_SPAM, SPAM = SPAM, NOT_SPAM
            else:
                NOT_SPAM, SPAM = 0, total_user_ids
        else: #bias in even
            if weight % 2 != 0:
                NOT_SPAM, SPAM = NOT_SPAM, SPAM
            else:
                NOT_SPAM, SPAM = total_user_ids, 0
    print(NOT_SPAM, SPAM)




def Naive(minX, maxX, neurons):
    SPAM, NOT_SPAM = 0, 0
    for X in range(int(minX), int(maxX) + 1):
        coefficient = X
        for (weight, bias) in neurons:
            coefficient = (weight * coefficient) + bias
        if coefficient % 2 != 0: #spam 
            SPAM += 1
        else: #not spam
            NOT_SPAM += 1
    print(NOT_SPAM, SPAM)


def userInput():
    test_cases = int(input())
    for case in range(test_cases):
        N, minX, maxX = input().split()
        neurons = []
        for neuron_layer in range(int(N)):
            weight, bias = input().split()
            neurons += [(int(weight), int(bias))]
        Compute(int(minX), int(maxX), neurons)


userInput()

