class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(numbers)):
            numMap[numbers[i]] = i
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if (complement in numMap and numbers[complement] != i):
                return [numbers[i], complement]
        return []
        