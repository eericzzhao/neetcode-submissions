class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l,r = 0, len(nums) - 1
        mid = r - 1
        fin = []
        while l < r and mid > l:
            two_sum = nums[l] + nums[r] 
            while l < r and mid > l: 
                three_sum = two_sum + nums[mid]
                if three_sum == 0:
                    fin.append([nums[l], nums[r], nums[mid]])
                    r -= 1
                    mid -= 1
                else:
                    mid -= 1
            r -= 1
            mid = r - 1

        return fin