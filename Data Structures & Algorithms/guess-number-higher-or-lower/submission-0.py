# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        L = 1
        H = n
        
        while L <= H:
            M = (H + L)//2
            res = guess(M)
            if res == -1:
                H = M - 1
            elif res == 1:
                L = M + 1
            else:
                return M