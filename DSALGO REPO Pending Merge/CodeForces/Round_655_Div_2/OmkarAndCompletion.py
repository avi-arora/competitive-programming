def series(n):
    data, x = [1], 1
    for _ in range(0,n-1):
        x += 2
        if x > 1000:
            x= 1
        data.append(x)
    return data

def improved(n):
    return [1] * n


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        for _ in range(n):
            print(1, end=" ")
        print()