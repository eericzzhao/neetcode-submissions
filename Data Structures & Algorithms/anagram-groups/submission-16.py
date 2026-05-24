class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = {}
        final = []

        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in sortedMap:
                final[sortedMap[sorted_str]].append(s)
            else:
                sorted_map[sorted_str] = len(final)
                final.append([s])

        return final