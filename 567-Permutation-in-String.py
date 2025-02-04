class Solution(object):
    def checkInclusion(self, s1, s2):
        \\\
        :type s1: str
        :type s2: str
        :rtype: bool
        \\\
        if len(s1) > len(s2):
            return False

        p_count = Counter(s1)
        s_count = Counter(s2[:len(s1)])
        if p_count == s_count:
            return True
            
        for i in range(len(s2) - len(s1)):
            if s_count[s2[i]] > 1:
                s_count[s2[i]] -= 1
            else: del s_count[s2[i]] 
            if s2[i+len(s1)] not in s_count:
                s_count[s2[i+len(s1)]] = 1
            else: s_count[s2[i+len(s1)]] += 1
            if p_count == s_count:
                return True
        return False
            
            
        

        