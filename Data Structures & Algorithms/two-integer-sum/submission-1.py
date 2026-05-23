class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            compl = target - nums[i]

            if compl in hashMap:
                return [hashMap[compl], i]
            hashMap[nums[i]] = i