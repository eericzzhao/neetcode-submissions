class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        
        for i in range(len(nums)):
            variable = target - nums[i]
            if variable in hashMap:
                return [hashMap[variable], i]
            hashMap[nums[i]] = i
        