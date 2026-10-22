class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currMax = -1 
        for i in range(len(arr)-1, -1, -1):
            aux = arr[i]
            arr[i] = currMax
            currMax = max(aux, currMax)
        return arr