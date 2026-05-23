class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapOrder = {}
        fin = []

        for s in strs:
            # goes through each string and reorders it in a ordered manner
            sorted_str = ''.join(sorted(s))
            # if we see that our sorted string is already contained in our map
            if sorted_str in mapOrder:
                # it's safe to say that we can append the string to the final list that it corresponds to in our map
                fin[mapOrder[sorted_str]].append(s)
            else:
                # then we can just send this sorted string to the very end 
                mapOrder[sorted_str] = len(fin)
                # we can just append our string to anywhere in our final answer
                fin.append([s])

        return fin
        