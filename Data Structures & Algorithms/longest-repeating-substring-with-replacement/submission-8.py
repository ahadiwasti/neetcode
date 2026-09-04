class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        currlen, maxlen = 0,0
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char,0)
            currlen = max(window[char], currlen)

            if (r-l+1)-currlen > k:
                window[s[l]]-=1
                l+=1


            maxlen = max(maxlen,r-l+1)

        return maxlen


