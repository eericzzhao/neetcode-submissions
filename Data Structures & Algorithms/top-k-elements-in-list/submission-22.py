class Solution:
    def topKFrequent(slef, nums: List[int], k:int ) -> List[int]:
        # freq = {}

        # # gets us the count of each value in the nums list
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1

        # # this reorders it such that we can sort it
        # arr = []
        # for val,count in freq.items():
        #     arr.append([count, val])
        # arr.sort()

        # # we can now append it to our target amount
        # temp = []
        # while len(temp) < k:
        #     temp.append(arr.pop()[1])
        # return temp
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        arr = []
        for val,cnt in freq.items():
            arr.append([cnt, val])
        arr.sort()

        temp = []
        while len(temp) < k:
            temp.append(arr.pop()[1])
        return temp
