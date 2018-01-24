#####################################
# SPAMCLAS: CODECHEF
#####################################

def Compute(minX, maxX, neurons):
    pass

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



userInput()

