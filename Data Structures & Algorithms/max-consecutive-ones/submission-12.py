class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = 0
        consecutive_ones = 0
        is_consecutive = True

        for i in range(len(nums)):
            #
            if nums[i]==1:
                consecutive_ones+=1    
            else:
                consecutive_ones = 0
            if consecutive_ones > max_consecutive_ones:
                max_consecutive_ones = consecutive_ones

        return(max_consecutive_ones)

    