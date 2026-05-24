class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapOrder = {}
        ans = []

        for s in strs:
            sorted_string = ''.join(sorted(s))
            if sorted_string in mapOrder:
                ans[mapOrder[sorted_string]].append(s)
            else:
                mapOrder[sorted_string] = len(ans)
                ans.append(s)

        return ans


        