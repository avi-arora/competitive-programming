class Solution:
    def countEven(self, num: int) -> int:
        # if digit sum is odd 
        # then the answer will be (num-1) // 2
        # if digit is even then num // 2
        # why 
        return (num-1) // 2 if sum(int(c) for c in str(num)) % 2 else num // 2