class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapOrder = {}
        final = []

        # iterate through every string
        for s in strs:
            # sort through every string 
            sorted_str = ''.join(sorted(s))
            # if our sorted string is in our final list of 
            if sorted_str in mapOrder:
                final[mapOrder[sorted_str]].append(s)
            else:
                mapOrder[sorted_str] = len(final)
                final.append([s])
                # needs more processing

        return final 


        