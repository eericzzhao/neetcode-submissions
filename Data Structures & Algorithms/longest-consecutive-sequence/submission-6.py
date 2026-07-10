class Solution:
    def longestConsecutive(self, nums:List[int]) -> int:
        # usage of a set for fast lookup time
        numSet = set(nums)
        longest = 0 # temp variable to store the longest length

        for i in numSet: # iterate through eveyr number
            # over here, we're checking if its 
            if (i - 1) not in numSet:
                curr_length = 0
                while (i + curr_length) in numSet:
                    curr_length += 1
                longest = max(curr_length, longest)
        return longest