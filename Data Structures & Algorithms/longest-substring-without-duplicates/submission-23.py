class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0

        reslen = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1

            seen.add(s[r])
            reslen = max(r-l+1,reslen)

        return reslen