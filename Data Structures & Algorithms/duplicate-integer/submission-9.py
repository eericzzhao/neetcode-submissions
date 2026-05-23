class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        hashset = set() # unordered unique list 

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
        