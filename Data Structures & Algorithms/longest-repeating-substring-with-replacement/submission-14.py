class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr = reslen = l = 0

        seen = {}

        for r in range(len(s)):
            seen[s[r]] = 1 + seen.get(s[r],0)

            curr = max(curr,seen.get(s[r]))

            while (r-l+1)-curr > k:
                seen[s[l]]-=1
                l+=1

            reslen = max(reslen, r-l+1)

        return reslen


