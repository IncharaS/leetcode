class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        sum = 0
        for i in nums:
            if i in dict:
                sum += dict[i]
                dict[i] += 1
            else:
                dict[i] = 1
        return sum