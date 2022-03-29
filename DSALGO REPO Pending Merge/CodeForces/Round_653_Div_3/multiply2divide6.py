
def bruteforce(n):
    result, totalMoves = n, 0
    while result != 1:
        if result % 6 == 0:
            result //= 6
        else: 
            result *= 2
        totalMoves += 1
    return totalMoves

def improved(n):
    result, totalMoves = n, 0
    while result != 1 and result != 0:
        if (result % 2 != 0 or result % 3 != 0):
            result *= 2
            if sumOfDigit(result) % 3 != 0:
                return -1
        else: 
            result //= 6

        totalMoves += 1
    return totalMoves



def sumOfDigit(n):
    sum = 0
    if n <= 9: 
        return n
    else: 
        sum = 0
        while n > 0:
            sum, n = n%10, n // 10
    return sum
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(bruteforce(n))
