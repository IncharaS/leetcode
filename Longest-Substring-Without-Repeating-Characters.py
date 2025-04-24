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
        chars = set()
        max_l = 0
        while i < len(s) and j < len(s):
            if s[j] not in chars:
                chars.add(s[j])
                max_l = max(max_l, j - i + 1)
                j += 1
            else:
                while s[j] in chars:
                    chars.remove(s[i])
                    i += 1
        return max_l
            