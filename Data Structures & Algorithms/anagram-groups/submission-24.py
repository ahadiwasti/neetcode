class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ditty = defaultdict(list)
        for word in strs:
            freq = [0]*26
            for char in word:
                freq[ord('a')-ord(char)]+=1

            ditty[tuple(freq)].append(word)

        return list(ditty.values())

        
        # res = []

        # for items in ditty.items():
        #     for item in items:
        #         res.append()

