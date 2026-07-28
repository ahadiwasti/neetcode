class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        l = r = have = need = 0
        window,freq={},{}
        
        for char in t:
            freq[char] = 1+freq.get(char,0)

        res,resLen = [-1,-1],float('inf')
        need = len(freq)
        while r < len(s):
            c = s[r]

            window[c] = 1+window.get(s[r],0)

            if c in freq and window[c] == freq[c]:
                have +=1

            while need == have:
                if r-l+1 < resLen:
                    res = [l,r+1]
                    resLen = r-l+1

                window[s[l]]-=1
                if s[l] in freq and window[s[l]] < freq[s[l]]:
                    have -=1
                l+=1
            r+=1
        i,j = res
        return s[i:j] if resLen != float('inf') else ""
                
