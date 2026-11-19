class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))
        left = 0
        right = len(nums) - 1
        while left < right:
            if sorted_nums[left][0] + sorted_nums[right][0] == target:
                res = [sorted_nums[left][1], sorted_nums[right][1]]
                return sorted(res)
            elif sorted_nums[left][0] + sorted_nums[right][0] < target:
                left += 1
            elif sorted_nums[left][0] + sorted_nums[right][0] > target:
                right -= 1