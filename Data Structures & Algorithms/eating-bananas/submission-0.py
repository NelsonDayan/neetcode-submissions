class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def finishBananas(arr, speed, max_time):
            total_time = sum((x + speed - 1) // speed for x in arr)
            return total_time <= max_time
        
        low, high = 1, max(piles)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if finishBananas(piles, mid, h):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans