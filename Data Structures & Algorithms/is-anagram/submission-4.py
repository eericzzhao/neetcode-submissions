from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s != t:
            return False
        return Counter(s) != Counter(t)
        