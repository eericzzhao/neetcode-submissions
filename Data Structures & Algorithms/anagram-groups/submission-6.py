class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapOrder = {}
        fin = []

        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in mapOrder:
                fin[mapOrder[sorted_str]].append(s)
            else:
                mapOrder[sorted_str] = len(fin)
                fin.append([s])

        return fin

        