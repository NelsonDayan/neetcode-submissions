class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix) == 0:
            return False
        def BinarySearch(arr, L, R, target):
            while L <= R:
                M = (L+R)//2
                print(M)
                if target < arr[M]:
                    R = M-1
                elif target > arr[M]:
                    L = M+1
                else:
                    return M
            return R
        FirstColumnList = []
        for x in matrix:
            FirstColumnList.append(x[0])
        print(FirstColumnList)
        print(BinarySearch(FirstColumnList, 0, len(FirstColumnList) - 1, target))
        col = BinarySearch(FirstColumnList, 0, len(FirstColumnList) - 1, target)
        row = BinarySearch(matrix[col], 0, len(matrix[col]) - 1, target)
        if matrix[col][row] == target:
            return True
        return False