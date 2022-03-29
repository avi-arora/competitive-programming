
def brute_force(data, l):
    check = 0
    while l != 1:
        i = 0
        while i < (l-1):
            if data[i] < data[i+1]:
                #decide which element to delete
                if i > 0 and data[i-1] < data[i+1]:
                    data.pop(i)
                else:
                    data.pop(i+1)
                check -= 1
                l -= 1
            else:
                i += 1
        check += 1
        
        if check > 1:
            break
    
    if l == 1:
        return "YES"
    else:
        return "NO"


def improved(data, l):
    if data[0] < data[l-1]: 
        return "YES"
    else:
        return "NO"


def reduceUsingImproved(data, l):
    pass

        



        


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        l = int(input())
        data = [int(d) for d in input("").split(" ")]
        print(improved(data, l))
