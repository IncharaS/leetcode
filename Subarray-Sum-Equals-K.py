class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        summ = 0
        result = 0
        for i in nums:
            summ += i
            diff = summ-k
            if diff in d:
                result += d[diff]
            d[summ] = d.get(summ, 0) + 1
        return result