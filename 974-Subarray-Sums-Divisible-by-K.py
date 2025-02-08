class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_ = 0
        dict_ = {0: 1}
        count = 0
        for i in nums:
            sum_ += i
            if sum_%k in dict_:
                count += dict_[sum_%k]
            dict_[sum_%k] = dict_.get(sum_%k, 0) + 1
        return count
            
            
