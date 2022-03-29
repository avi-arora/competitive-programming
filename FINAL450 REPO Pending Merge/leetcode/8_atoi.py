class Solution:
    def myAtoi(self, s: str) -> int:
        #count leading whitespaces
        i = 0
        while i < len(s) and s[i] == " ":
            i+=1
        
        #remove leading space
        s = s[i:]
        
        i, numInStr = 0, ""
        isPositive = True
        signEncountered = 0
        while i < len(s):
            c = s[i]
            if ord(c) >= ord('0') and ord(c) <= ord('9') and signEncountered <= 1:
                numInStr += c
            elif c == "-" and signEncountered == 0 and len(numInStr) == 0:
                isPositive = False
                signEncountered += 1
            elif c == "+" and signEncountered == 0 and len(numInStr) == 0:
                signEncountered += 1
            else:
                break
            i+=1
        
        result, totalDigits = 0, len(numInStr)
        i = 0
        while i < len(numInStr):
            result += int(numInStr[i]) * pow(10,totalDigits-1)
            i, totalDigits = i+1, totalDigits-1
        
        #perform validation
        if not isPositive: 
            result = -result
        
        #perform limit validation 
        if result >= -pow(2,31) and result <= pow(2,31)-1:
            return result
        elif isPositive:
            return pow(2,31)-1
        else:
            return -pow(2,31)

    def myAtoiPy(self, s: str) -> int:
          """
          Atio using py approach
          """
          pass
            



if __name__ == "__main__":
    obj = Solution()
    print(obj.myAtoi("+1"))