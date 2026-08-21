class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        maxlen, currlen = 0,0
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = 1+window.get(char,0)

            currlen = max(window[char],currlen)

            while (r-l+1)-currlen > k:
                window[s[l]]-=1
                l+=1
            
            maxlen= max(r-l+1,maxlen)

        return maxlen
