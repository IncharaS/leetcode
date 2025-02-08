class Solution(object):
    def subarraySum(self, nums, k):
        res = 0
        freq_dict = {0:1}
        sum_ = 0
        for i in nums:
            sum_ += i
            if sum_ - k in freq_dict:
                res += freq_dict[sum_ - k]
            freq_dict[sum_] = freq_dict.get(sum_,0) + 1
        return res

