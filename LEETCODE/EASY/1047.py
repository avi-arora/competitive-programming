class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            #check if top of stack contains the same element
            #if yes, then don't append it to the result
            if len(stack) > 0 and stack[len(stack)-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
                
        
        