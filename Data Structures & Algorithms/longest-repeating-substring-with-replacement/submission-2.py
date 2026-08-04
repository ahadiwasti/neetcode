class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxsum,currsum = 0,0
        l,r=0,0
        freq={}
        while r < len(s):
            char = s[r]
            freq[char] = 1+freq.get(char,0)
            currsum = max(currsum,freq[char])
            while (r-l+1)-currsum > k:
                freq[s[l]] -=1
                l+=1
            maxsum = max(maxsum, r-l+1)
            r+=1
        return maxsum

        # maxsum,currsum = 0,0
        # l=0
        # freq = {}
        
        # for r in range(len(s)):
        #     freq[s[r]] = 1+ freq.get(s[r],0)
        #     currsum = max(currsum,freq[s[r]])
        #     while (r-l+1)-currsum > k:
        #         freq[s[l]] -=1
        #         l+=1
        #     maxsum = max(maxsum,r-l+1)
        # return maxsum