class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(top, bottom):
            while top <= bottom:
                mid = (bottom + top) // 2
                if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                    return mid
                elif matrix[mid][0] > target:
                    bottom = mid - 1
                else: top = mid + 1
            return -1
        def bs_across(l, r, index):
            while l <= r:
                mid = (r + l) // 2
                if matrix[index][mid] == target:
                    return True
                elif matrix[index][mid] < target:
                    l = mid + 1
                else: r = mid - 1
            return False

        index = bs(0, len(matrix) - 1)
        print(index)
        if index == -1: 
            return False
        else:
            print(index)
            return bs_across(0, len(matrix[0]) - 1, index)