class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window, freq = {}, {}

        for c in s1:
            freq[c] = 1 + freq.get(c,0)

        for r in range(len(s2)):
            char = s2[r]

            window[char] = 1 + window.get(char,0)

            if r >= len(s1):
                leftchar = s2[r-len(s1)]
                window[leftchar]-=1
                if window[leftchar] == 0:
                    del window[leftchar]
            
            if r >= len(s1)-1 and window == freq:
                return True

        return False
                    