class Solution:
    def encode(self, strs: List[str]) -> str:
        # set up a temporary string that we'll update
        res = ""
        # iterate through the ztriungs
        for s in strs:
            # concat it's string size + a delimiter + the actual string
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        # setup the new output list
        res = []
        i = 0
        # iterate through the entire string
        while i < len(s):
            j = i
            # j will be the end of the number
            while s[j] != '#':
                j += 1
            # we can convert that str into the number
            length = int(s[i:j])
            # continue on from there
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
