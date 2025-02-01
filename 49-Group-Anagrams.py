class Solution(object):
    def groupAnagrams(self, strs):
        \\\
        :type strs: List[str]
        :rtype: List[List[str]]
        \\\
        strs_dict = {}
        for _ in strs:
            sorted_s = ''.join(sorted(_)) 
            if sorted_s not in strs_dict:
                strs_dict[sorted_s] = []
            strs_dict[sorted_s].append(_)
        return list(strs_dict.values())

        return sorted_s
        