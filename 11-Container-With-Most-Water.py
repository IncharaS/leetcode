class Solution(object):
    def maxArea(self, height):
        \\\
        :type height: List[int]
        :rtype: int
        \\\
        left = 0
        area = 0
        right = len(height) - 1
        ## start and either ends and start moving towards each other
        while left < right:
            area_now = min(height[left], height[right]) * (right - left)
            area = max(area, area_now)
            print(area, area_now)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return area

        