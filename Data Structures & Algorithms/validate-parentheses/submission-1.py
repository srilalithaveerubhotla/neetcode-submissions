class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dicte ={')':'(', '}':'{', ']':'['}
        for i in s:
            if i in dicte:
                if stack and stack[-1]==dicte[i]:
                    stack.pop()
                else:
                    False
            else:
                stack.append(i)
        return True if not stack else False
        


                
        