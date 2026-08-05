class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        l=0
        seen=set()

        for r in range(len(s)):
            char = s[r]
            while char in seen:
                seen.remove(s[l])
                l+=1
            seen.add(char)
            maxlen = max(r-l+1,maxlen)

        return maxlen
