class Solution:
    def isValid(self, s: str) -> bool:
        validity=True
        stack=[]

        if s == []:
            return True

        for i in range(len(s)):
            if s[i] == '}':
                if stack == []:
                    validity=False
                    break
                if stack.pop() != '{':
                    validity=False
                    break
            elif s[i] == ']':
                if stack == []:
                    validity=False
                    break
                if stack.pop() != '[':
                    validity=False
                    break
            elif s[i] == ')':
                if stack == []:
                    validity=False
                    break
                if stack.pop() != '(':
                    validity=False
                    break
            else:
                stack.append(s[i])
                print(stack)

        if stack != []:
            validity = False
        
        return validity
