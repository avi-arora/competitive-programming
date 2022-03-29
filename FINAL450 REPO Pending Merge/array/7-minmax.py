
def minmax_linear(list):
    if len(list) == 1:
        max, min = list[0], list[0]
    else:
        if list[0] > list[1]:
            max, min = list[0], list[1]
        else:
            max, min = list[1], list[0]
        
        for i in range(2, len(list)):
            if list[i] > max:
                max = list[i]
            elif list[i] < min:
                min = list[i]
        
    return (min, max)


def minmax_tournamentmethod(list, start, end):
    """
    Uses recursive divide and conquer
    """
    min_e, max_e = list[0], list[0]
    #base case, if length is 1, return (min, max)
    if start == end:
        min_e, max_e = list[start], list[start]
        return (min_e, max_e)
    #another base case
    elif end == start + 1:
        if list[start] < list[end]:
            min_e, max_e = list[start], list[end]
        else:
            min_e, max_e = list[start], list[end]
        return (min_e, max_e)
    else:
        #find the mid point and use Divide and conquer 
        mid = (start+end) // 2
        min_left, max_left = minmax_tournamentmethod(list, 0, mid)
        min_right, max_right = minmax_tournamentmethod(list, mid+1, end)

        
        return (min(min_left, min_right), max(max_left, max_right))




def minmax_compareinpair(list):
    pass

def min_recursive(list, min_index, current_index):
    if current_index >= len(list):
        return list[min_index]
    if list[current_index] < list[min_index]:
        min_index = current_index
    return min_recursive(list, min_index, current_index+1)

def max_recursive(list, max_index, current_index):
    if current_index >= len(list):
        return list[max_index]
    if list[current_index] > list[max_index]:
        max_index = current_index
    return max_recursive(list, max_index, current_index+1) 


if __name__ == "__main__":
    list = [1,2,3,0,12,4,5]
   # print(minmax_linear(list))
   # print(min_recursive(list, 0, 1))
   # print(max_recursive(list, 0, 1))
    print(minmax_tournamentmethod(list, 0, len(list)-1))
    