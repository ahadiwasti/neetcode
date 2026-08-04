class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        currmax = 0
        seen = set()
        for r in range(len(s)):
            char = s[r]
            while char in seen:
                seen.remove(s[l])
                l+=1
            seen.add(char)
            currmax = max(currmax,r-l+1)
        return currmax

       
        # l = 0
        # currMax=0
        # seen={}
        # for r in range(len(s)):
        #     if s[r] in seen:
        #         l=max(l,seen[s[r]]+1)
        #     seen[s[r]] = r
        #     currMax = max(currMax,(r-l)+1)
        # return currMax            


