class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        curr = reslen = l = 0

        for r in range(len(s)):
            seen[s[r]] = 1 + seen.get(s[r],0)
            curr = max(seen[s[r]], curr)

            while (r-l+1)-curr > k:
                seen[s[l]]-=1
                l +=1
            reslen = max((r-l+1),reslen)

        return reslen