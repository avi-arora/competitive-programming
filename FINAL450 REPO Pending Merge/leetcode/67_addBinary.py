class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena,lenb = len(a), len(b)
        if lena > lenb:
            b = '0'* (lena-lenb) + b
        elif lenb > lena:
            a = '0' * (lenb-lena) + a
        
        result, carry = "", 0
        i = max(lena,lenb)-1
        while i >= 0:
            if a[i] == '1' and b[i] == '1':
                if c==1:
                    result = "1" + result
                else:
                    result = "0" + result
                    carry = 1
            elif a[i] == '1' or b[i] == '1':
                if carry == 1:
                    result = "0" + result
                else:
                    result = "1" + result
            else:
                if carry == '1':
                    result = "1" + result
                    carry = 0
                else:
                    result = "0" + result
            i-=1
        if carry == 1:
            result = "1" + result
            
        return result

            



if __name__ == "__main__":
    obj = Solution()
    print(obj.addBinary("101","11"))


