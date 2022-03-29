import math

def largeFactorial(n):
    """
    Returns factorail of a large number
    using decomposition technique
    """
    def multiply(result,size,num):
        carry = 0
        for x in range(size):
            product = result[x] * num + carry
            result[x] = product % 10
            carry = product // 10
        
        while carry:
            result[size] = carry % 10
            carry = carry // 10
            size += 1
        
        return size

    #result up to 500 digits
    result,size = [1] * 500, 1

    for num in range(2, n+1):
        size = multiply(result,size,num)

    return int("".join([str(n) for n in result[size-1::-1]]))
    

def CountFactorialDigits(n):
    """
    Returns number of digits in factorialEfficient
    """
    def naive(n):
        """
        algorithm: count factorial then individual digits
        """
        factN, counter = factorialIterative(n),0
        while factN: 
            counter+=1
            factN = factN // 10
        return counter 

    def usingLog(n):
        sum = 0
        for n in range(2,n+1):
            sum += math.log10(n)
        return math.floor(sum)

    def improved(n):
        """
        uses  Kamenetsky’s formulae
        """
        return math.floor((n * (math.log10(n/math.e))) + (math.log10(2*math.pi*n)/2))+1
    
    return improved(n)

def factorialEfficient(n):
    pass


def factorialRecursive(n):
    if n <= 1:
        return 1
    else:
        return factorialRecursive(n-1) * n


def factorialIterative(n):
    result = 1
    for num in range(n,1,-1):
        result *= num
    return result



if __name__ == "__main__":
    print(CountFactorialDigits(10))