
def brute_force(n, x, y):
    while n >= 0:
        if n % x == y:
            return n
        n -= 1

    return n


def improved(n, x, y):
    i = n // x
    while i >= 0:
        num = (i*x) + y
        if num <= n and num % x == y:
            return num
        i -= 1
    return i


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x, y, n = map((int), input().split(" "))
        i = n // x
        while i >= 0:
            num = (i*x) + y
            if num <= n and num % x == y:
                print(num)
                break
            i -= 1
