class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        \\\
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        \\\
        a = Counter(ransomNote)
        b = Counter(magazine)

        for i in a:
            if i not in b:
                return False
            if a[i] > b[i]:
                return False
        return True
        