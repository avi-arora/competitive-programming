

def fibRecursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibRecursive(n-1) + fibRecursive(n-2)


def fibIterative(n):
    prev, curr = 0, 1
    i,next = 0, 0
    while i < n-1:
        next = prev + curr
        prev, curr = curr, next
        i+=1
    return next

def fibDPTopDown(n, memory):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif len(memory) > n:
        return memory[n]
    else:
        num = fibDPTopDown(n-1, memory) + fibDPTopDown(n-2, memory)
        memory.append(num)
        return memory[n]
    

def fibDPBottomUp(n):
    memory = [0] * (n+1)
    memory[1] = 1
    i = 2
    while i <= n:
        memory[i] = memory[i-1] + memory[i-2]
        i+=1
    return memory[n]


def fibUsingMatrixMultiply(n):
    """
    Computes nth fibonacii number using matrix multiplication
    Algorithm:
    let M = [[1,1],[1,0]]
    Soln: Pow(M,n-1) then f[0][0] is the n+1 fibonacii number
    Reasoning:
    | fn+1 fn   |
    | fn   fn-1 |

    TC: O(n)
    SC: O(1)
    """ 

    fibMatrix = [[1,1],[1,0]]
    def multiply(matrix):
        a = matrix[0][0] * fibMatrix[0][0] + matrix[0][1] * fibMatrix[1][0]
        b = matrix[0][0] * fibMatrix[0][1] + matrix[0][1] * fibMatrix[1][1]
        c = matrix[1][0] * fibMatrix[0][0] + matrix[1][1] * fibMatrix[1][0]
        d = matrix[1][0] * fibMatrix[0][1] + matrix[1][1] * fibMatrix[1][1]
        return [[a,b],[c,d]]
    
    matrix = [[1,1],[1,0]]
    for _ in range(2,n):
        matrix = multiply(matrix)

    return matrix[0][0]



if __name__ == "__main__":
    print(fibRecursive(5))
    print(fibIterative(5))
    print(fibDPBottomUp(5))
    print(fibDPTopDown(5,[0,1]))
    print(fibUsingMatrixMultiply(7))
