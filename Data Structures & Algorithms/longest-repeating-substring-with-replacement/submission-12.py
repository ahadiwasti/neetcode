class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        reslen = 0
        curr = 0
        window = {}
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            curr = max(curr,window[s[r]])

            while (r-l+1)-curr > k:
                window[s[l]] -=1
                l+=1
            
            reslen = max(r-l+1,reslen)

        return reslen



