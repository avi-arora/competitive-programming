

def twoSumBruteForce(nums, target):
    """
    Uses a brute force technique to solve the twosum problem
    TC: O(n^2)
    SC: O(1)
    """
    for i in range(len(nums)-1):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]

def twoSumEfficientTwoPass(nums, target):
    """
    Complement based approach with using extra space 
    TC:O(n)
    SC:O(n)
    what is complement = target - nums[i]
    e.g let's say target = 9, then perfect complement would be 9 - 7 = 2 and 2 is present in the list 
    """
    dict = {}
    for i in range(len(nums)):
        dict[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dict and dict[complement] != i:
            return [i, dict[complement]]
    
def twoSumEfficient(nums, target):
    """
    Uses complement based approach but with one single pass
    TC:O(n)
    SC:O(n)
    """
    dict = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if(complement in dict):
            return [i, dict[complement]]
        dict[nums[i]] = i
    


if __name__ == "__main__":
    print(twoSumBruteForce([2,7,11,15], 9))
    print(twoSumEfficientTwoPass([2,7,11,15], 9))
    print(twoSumEfficient([2,7,11,15], 9))
    