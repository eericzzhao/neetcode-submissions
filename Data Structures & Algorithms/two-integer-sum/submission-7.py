class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        # hashmap to store the keys and indice value

        for i in range(len(nums)):
            numMap[nums[i]] = i

        # iterating through the entire nums array list
        for i in range(len(nums)):
            complement = target - nums[i]
            # if the complement EXISTS and
            # if the indice of the complement is not the indice that we are looking at
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
            

        return []