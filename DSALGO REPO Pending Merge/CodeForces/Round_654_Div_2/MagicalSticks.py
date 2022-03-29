

def countSticks(n):
    start, end = 1, n-1
    counter = 1
    while start + end == n and start < end and end > start:
        counter += 1
        start, end = start + 1, end - 1
    
    return counter


def shortcut(n):
    # even 
    if n%2 == 0:
        return n//2
    else:
        return n//2 + 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n%2 == 0:
            print(n//2)
        else:
            print(n//2 + 1)