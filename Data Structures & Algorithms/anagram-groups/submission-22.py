class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti = defaultdict(list)

        for word in strs:
            freq = [0]*26
            for char in word:
                freq[ord(char)-ord('a')]+=1
            dicti[tuple(freq)].append(word)

        return list(dicti.values())