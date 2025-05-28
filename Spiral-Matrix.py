class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        output = []

        while top <= bottom and left <= right:
            # Traverse from Left to Right
            for j in range(left, right + 1):
                output.append(matrix[top][j])
            top += 1
            
            # Traverse Downwards
            for i in range(top, bottom + 1):
                output.append(matrix[i][right])
            right -= 1
            
            # Traverse from Right to Left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    output.append(matrix[bottom][j])
                bottom -= 1
            
            # Traverse Upwards
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])
                left += 1

        return output
