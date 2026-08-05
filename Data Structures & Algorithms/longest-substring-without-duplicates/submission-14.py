class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        seen= set()
        maxlen=0

        for r in range(len(s)):
            char = s[r]

            while char in seen:
                seen.remove(s[l])
                l+=1

            seen.add(char)
            maxlen = max(maxlen,r-l+1)

        return maxlen