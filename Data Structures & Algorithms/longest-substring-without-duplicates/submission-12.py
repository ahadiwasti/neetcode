class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        currsum = 0

        seen = set()

        for r in range(len(s)):
            char = s[r]
            while char in seen:
                seen.remove(s[l])
                l+=1
            
            seen.add(char)

            currsum = max(currsum,r-l+1)

        return currsum