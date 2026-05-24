class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapOrder = {}
        final = []

        for s in strs:
            sorted_str = ' '.join(sorted(s)) 
            if sorted_str in mapOrder:
                final[mapOrder[sorted_str]].append(s)
            else:
                mapOrder[sorted_str] = len(final)
                final.append(s) 
        return final


        