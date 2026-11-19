class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)

        index = 0
        while index < len(nums)-1:
            if sorted_nums[index] == sorted_nums[index+1]: 
                return True
            index+=1
        return False