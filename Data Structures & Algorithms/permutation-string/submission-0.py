class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq,window = {},{}
        for char in s1:
            freq[char] = 1+freq.get(char,0)
        for r in range(len(s2)):
            window[s2[r]] = 1+window.get(s2[r],0)

            if r >= len(s1):
                left_char = s2[r-len(s1)]
                window[left_char] -=1

                if window[left_char] == 0:
                    del window[left_char]
            
            if r >= len(s1) -1 and window == freq:
                return True
        return False
