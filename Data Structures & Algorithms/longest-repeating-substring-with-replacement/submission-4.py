class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        reslen,currlen = 0,0

        l,r=0,0

        mp = {}

        while r < len(s):
            char = s[r]
            mp[char] = 1+mp.get(char,0)
            currlen = max(currlen,mp[char])
            if (r-l+1)-currlen > k:
                mp[s[l]]-=1
                l+=1
            reslen = max(reslen,r-l+1)
            r+=1
        return reslen