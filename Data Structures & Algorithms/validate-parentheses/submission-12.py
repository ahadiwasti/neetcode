class Solution:
    def isValid(self, s: str) -> bool:
        btof = {")":"(","]":"[","}":"{"}
        seen = []

        for b in s:
            if b in btof:
                if seen and seen[-1] == btof[b]:
                    seen.pop()
                else:
                    return False
            else:
                seen.append(b)

        return True if not seen else False