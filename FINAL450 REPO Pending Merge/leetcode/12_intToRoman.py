class Solution:
    def intToRoman(self, num: int) -> str:    
        roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX',10: 'X',40: 'XL' , 50: 'L', 90: 'XC',100: 'C', 400: 'CD',500: 'D', 900: 'CM', 1000: 'M'}
        result = "" 
        while num != 0:
            for k in range(len(roman)-1,-1,-1):
                number = list(roman.keys())[k]
                if number <= num:
                    num -= number
                    result += roman[number]
                    break
        return result 
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.intToRoman(1994))

