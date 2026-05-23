class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        # we're establishing the buckets here 
        final = [[] for i in range(len(nums) + 1)]
        
        # we're iterating through the nums to get a total value
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        # let's iterate through the items and get the key and values 
        for num,count in freq.items():
            # based on the number of times, let's append the attached value
            final[count].append(num)
            print(final)
            
        res = []
        for i in range(len(final) - 1, 0, -1):
            for num in final[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return final
