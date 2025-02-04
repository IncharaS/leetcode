from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        \\\
        :type s: str
        :type p: str
        :rtype: List[int]
        \\\
        if len(p) > len(s):
            return []

        result = []
        p_count = Counter(p)
        s_count = Counter(s[:len(p)])
        if p_count == s_count:
            result.append(0)
            
        for i in range(len(s) - len(p)):
            if s_count[s[i]] > 1:
                s_count[s[i]] -= 1
            else: del s_count[s[i]] 
            if s[i+len(p)] not in s_count:
                s_count[s[i+len(p)]] = 1
            else: s_count[s[i+len(p)]] += 1
            if p_count == s_count:
                result.append(i+1)
        return result
            
            
        