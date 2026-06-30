class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for char in strs:
            freq = [0]*26
            for x in char:
                freq[ord(x)-ord('a')]+=1
            res[tuple(freq)].append(char)
        return list(res.values())