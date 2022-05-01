class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = int("".join([str((ord(c)%97)+1) for c in s]))
        count = 0
        while count < k:
            result = 0
            while s > 0:
                result += s % 10
                s = s // 10
            s = result
            count += 1
        
        return result
        