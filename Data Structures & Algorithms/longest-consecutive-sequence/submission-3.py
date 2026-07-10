class Solution:
    def longestConsecutive(self, nums:List[int]) -> int:
        numSet = set(nums)
        longest = 0 

        for i in numSet:
            curr_length = 0
            while (i + curr_length) in numSet:
                curr_length += 1
            longest = max(curr_length, longest)
        return longest