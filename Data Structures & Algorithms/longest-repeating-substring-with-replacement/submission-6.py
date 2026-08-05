class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window={}
        l=0
        currlen,maxlen = 0,0

        for r in range(len(s)):
            char = s[r]
            window[char] = 1+window.get(char,0)
            currlen = max(currlen,window[char])

            if (r-l+1)-currlen > k:
                window[s[l]]-=1
                l+=1

            maxlen = max(maxlen,r-l+1)

        return maxlen