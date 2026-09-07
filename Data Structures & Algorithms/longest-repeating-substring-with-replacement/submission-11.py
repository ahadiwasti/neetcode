class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        currlen, maxlen = 0, 0 
        l = 0
        window = {}
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            currlen = max(currlen, window[s[r]])

            if (r-l+1)-currlen > k:
                window[s[l]]-=1
                l+=1
            
            maxlen = max(r-l+1,maxlen)
        return maxlen


