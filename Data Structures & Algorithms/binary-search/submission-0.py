class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return -1
        def BinarySearch(arr, L, R, value):
            if L > R:
                return -1
            M = (L + R) // 2
            if value < arr[M]:
                return BinarySearch(arr, L, M - 1, value)
            elif value > arr[M]:
                return BinarySearch(arr, M + 1, R, value)
            else:
                return M
        
        return BinarySearch(nums, 0, len(nums) - 1, target)