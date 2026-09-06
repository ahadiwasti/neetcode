class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        currlen = maxlen = 0
        window = {}
        l=0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            currlen = max(window[s[r]],currlen)

            if (r-l+1)-currlen > k:
                window[s[l]] -=1
                l+=1
            maxlen = max(r-l+1,maxlen)

        return maxlen