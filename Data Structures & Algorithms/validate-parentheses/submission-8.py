class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        if s == []:
            return True

        for i in range(len(s)):
            if s[i] == '}':
                if stack == []:
                    return False
                if stack.pop() != '{':
                    return False
            elif s[i] == ']':
                if stack == []:
                    return False
                if stack.pop() != '[':
                    return False
            elif s[i] == ')':
                if stack == []:
                    return False
                if stack.pop() != '(':
                    return False
            else:
                stack.append(s[i])
                print(stack)

        if stack != []:
            return False
        
        return True