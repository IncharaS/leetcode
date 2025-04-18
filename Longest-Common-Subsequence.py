class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text2)
        l2 = len(text1)
        matrix = [[0] * (l2 + 1) for _ in range(l1 + 1)]

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text2[i - 1] == text1[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1] + 1
                else:
                    matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

        return matrix[l1][l2]
