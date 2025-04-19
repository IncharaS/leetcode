class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # st = set()
        # l, r = 0, 0
        # n = len(s)
        # leng = 0
        # while l <= r and r < n:
        #     while l < r and  s[r] in st:
        #         st.remove(s[l])
        #         l += 1
        #     st.add(s[r])
        #     length = r - l + 1
        #     r += 1
        #     leng = max(leng, length)
        #     print(leng)
        
        # return leng
        # d = [-1] * 172
        # l, r = 0, 0
        # n = len(s)
        # length = 0
        # while l <= r and r < n:
        #     if d[ord(s[r])] != -1:
        #         l = max(d[ord(s[r])] + 1, l)
        #     d[ord(s[r])] = r
        #     length = max(length, r - l + 1)
        #     r += 1
        # return length
        i, j = 0, 0
        l = len(s)
        char = set()
        res = 0
        if l == 0: return 0
        while i < l and j < l:
            while j < l and s[j] in char:
                char.remove(s[i])
                i += 1
            while j < l and s[j] not in char:
                char.add(s[j])
                res = max(res, j - i + 1)
                j += 1
            
            
        return res 
