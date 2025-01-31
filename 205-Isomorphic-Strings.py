class Solution(object):
    def isIsomorphic(self, s, t):
        \\\
        :type s: str
        :type t: str
        :rtype: bool
        \\\
        s_, t_ = {}, {}
        for i in range(len(s)):
            a, b = s[i], t[i]
            if (a in s_ and s_[a] != b) or (b in t_ and t_[b] != a):
                return False
            s_[a] = b
            t_[b] = a
        return True

                    