class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        mp = {"}":"{",")":"(","]":"["}

        for brac in s:
            if brac in mp:
                if seen and seen[-1] == mp[brac]:
                    seen.pop()
                else:
                    return False
            else:
                seen.append(brac)

        return True if not seen else False

            