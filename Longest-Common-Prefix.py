class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lc = strs[0]
        for i in range(1, len(strs)):
            j, k = 0, 0
            cw = strs[i]
            while j < len(cw) and k < len(lc) and cw[j] == lc[k]:
                j += 1
                k += 1
            lc = lc[:k]
        return lc
                