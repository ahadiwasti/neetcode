class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        reslen = 0
        curr = 0
        seen = {}
        l = 0
        for r in range(len(s)):
            seen[s[r]] = 1+ seen.get(s[r],0)
            curr = max(curr, seen[s[r]])

            while (r-l+1)-curr > k:
                seen[s[l]]-=1
                l+=1
            reslen = max(r-l+1,reslen)


                
        return reslen
            