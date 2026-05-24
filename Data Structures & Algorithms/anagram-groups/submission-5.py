class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapOrder = {}
        fin = []

        for s in strs:
            sorted_string = ''.join(sorted(s))
            if sorted_string in mapOrder:
                fin[mapOrder[sorted_string]].append(s)
            else:
                mapOrder[sorted_string] = len(fin)
                fin.append(s)

        return fin

        