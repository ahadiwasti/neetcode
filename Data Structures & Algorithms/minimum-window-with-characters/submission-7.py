class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, freq = {},{}
        need = have = l = r = 0
        reslen = float('inf')
        res = [-1,-1]

        for c in t:
            freq[c] = 1+freq.get(c,0)
        need = len(freq)

        while r < len(s):
            char = s[r]
            window[char] = 1+ window.get(char,0)

            if char in freq and window[char] == freq[char]:
                have+=1

            while need == have:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = [l,r+1]

                window[s[l]]-=1

                if s[l] in freq and window[s[l]] < freq[s[l]]:
                    have -=1
                l+=1
            r+=1
        i,j = res

        return s[i:j] if reslen != float('inf') else ""
    
       