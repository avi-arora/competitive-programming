

def powerRecursive(a, b):
    """
    Computes a^b recursively
    """
    if b == 0:
        return 1
    else:
        return a * powerRecursive(a, b-1)


def powerIterative(a, b):
    result = 1
    while b > 0:
        result *= a
        b -= 1
    return result


def powerDAC(a, b):
    """
    Uses Divide and Conquer Technique
    TC: O(n)
    SC: O(1)
    """
    if b == 0:
        return 1
    elif b%2==0:
        return powerDAC(a, b//2) * powerDAC(a, b//2)
    else:
        return (a * powerDAC(a, b//2)) * powerDAC(a, b//2)

def powerDACwithDP(a,b):
    """
    Uses Divide and Conquer and Memoization to improve
    TC: O(log n)
    SC: O(1)
    """
    if b == 0:
        return 1
    else:
        temp = powerDACwithDP(a, b//2)
        if b%2==0:
            return temp*temp
        else:
            return a*temp*temp


if __name__ == "__main__":
    print(powerRecursive(2,5))
    print(powerIterative(2,5))
    print(powerDAC(2,5))
    print(powerDACwithDP(2,5))