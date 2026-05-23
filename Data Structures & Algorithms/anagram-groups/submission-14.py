class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the dictionary containing the matching word
        mapOrder = {}
        # the final list containing the sublist of anagrams
        final = []

        # iterate through every string
        for s in strs:
            # sort through every string 
            sorted_str = ''.join(sorted(s))
            # if our sorted string matches with one of our sorted words
            if sorted_str in mapOrder:
                # We can add the original string into their respective list
                final[mapOrder[sorted_str]].append(s)
            else:
                # otherwise, we add the sorted word to the end of the map
                mapOrder[sorted_str] = len(final)
                # we can also append a new list with the original word 
                final.append([s])
        return final 


        