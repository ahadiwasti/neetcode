class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        l=r=0
        freq={}
        window={}
        for c in t:
            freq[c] = 1+freq.get(c, 0)
        
        have,need = 0, len(freq)
        res, resLen = [-1,-1], float('inf')

        while r < len(s):
            char = s[r]
            window[char] = 1+window.get(char,0)

            if char in freq and window[char] == freq[char]:
                have+=1

            while have == need:
                if r-l+1 < resLen:
                    res = [l,r]
                    resLen = r-l+1

                window[s[l]] -=1
                if s[l] in freq and window[s[l]] < freq[s[l]]:
                    have -=1

                l+=1
            r+=1

        l,r = res

        return s[l:r+1] if resLen != float('inf') else ""