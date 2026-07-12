class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxed = 0
        l,r = 0, len(heights) - 1
        while l < r:
            # this is just the width x height
            area = (r - l) * (min(heights[l], heights[r]))
            maxed = max(maxed, area)
            # here, we're just moving whatever box that we see is smaller 
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1

        return maxed 
