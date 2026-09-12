class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window,freq = {}, {}
        for c in t:
            freq[c] = 1 + freq.get(c,0)

        need = len(freq)
        have = l = 0

        reslen = float('inf')
        res = [-1,-1]

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)

            if s[r] in freq and window[s[r]] == freq[s[r]]:
                have +=1

            while have == need:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = [l,r+1]

                window[s[l]] -= 1

                if s[l] in freq and window[s[l]] < freq[s[l]]:
                    have -=1

                l+=1

        i,j= res

        return s[i:j] if reslen != float('inf') else ""

