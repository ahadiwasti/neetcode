class Solution:
    def groupAnagrams(self, strs)-> list[list[str]]:

        resp = defaultdict(list)

        for word in strs:
            freq = [0]*26
            for char in word:
                freq[ord('a')-ord(char)]+=1

            resp[tuple(freq)].append(word)

        return list(resp.values())