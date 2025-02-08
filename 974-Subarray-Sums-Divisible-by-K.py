class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        dictionary = {0:1}
        count = 0
        for i in nums:
            prefix_sum += i
            r = prefix_sum % k
            if r < 0:
                r += k
            if r in dictionary:
                count += dictionary[r]
            dictionary[r] = 1 + dictionary.get(r, 0) 
        return count
