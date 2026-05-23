class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups:defaultdict = defaultdict(list)
        answer = []

        for word in strs:
            sortedWord = ''.join(sorted(word))
            groups[sortedWord].append(word)

        for group in groups.values():
            answer.append(group)

        return answer