class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket = defaultdict(list)
        for word in strs:
            freq = [0]*26
            for c in word:
                freq[ord(c)-ord('a')]+=1
            bucket[tuple(freq)].append(word)

        return list(bucket.values())

# S:O(m*n)
# T:O(n)