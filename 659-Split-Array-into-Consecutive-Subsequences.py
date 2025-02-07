class Solution(object):
    def isPossible(self, nums):
        \\\
        :type nums: List[int]
        :rtype: bool
        \\\
        ## cant store the subarrays itself, so store freq and need of the numbers
        freq = Counter(nums)
        need = Counter()
        ## increase the need only once you confirm that 3 elements you need are already there in each subsequence
        for i in nums:
            if freq[i] == 0:
                continue
            if need[i] > 0:
                need[i] -= 1
                freq[i] -= 1
                need[i+1] += 1
            elif freq[i] > 0 and freq[i+1] > 0 and freq[i+2] > 0:
                need[i+3] += 1
                freq[i] -= 1
                freq[i+1] -= 1
                freq[i+2] -= 1
            else: return False
        return True



