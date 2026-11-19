class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlnum(char):
            return ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('0' <= char <= '9') 
        
        left=0
        right=len(s)-1

        while left < right:
            if not isAlnum(s[left]):
                left+=1
            elif not isAlnum(s[right]):
                right-=1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left+=1
                right-=1
        return True