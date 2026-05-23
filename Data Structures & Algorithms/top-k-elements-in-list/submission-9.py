class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialize a dictionary 
        count = {}

        # iterate through the nums list
        for num in nums:
            # get the total count of each number for each number
            count[num] = count.get(num,0) + 1
        
        # intiialize a list
        arr = []
        for num, count in count.items():
            # append all the tuples (with the count and then the number)
            arr.append([count, num])
        # this allows us to sort through the keys ascending
        arr.sort()

        res = []
        # we keep appending the numbers to the temporary array 
        while len(res) < k:
            # we stop at our k target 
            res.append(arr.pop()[1])
        return res
