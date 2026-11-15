class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs:
            freq = [0]*26
            for char in word:
                freq[ord('a')-ord(char)]+=1

            group[tuple(freq)].append(word)

        return list(group.values())