class Solution:
    def isValid(self, s: str) -> bool:
        backtofront = {")":"(","]":"[","}":"{"}
        seen = []

        for b in s:
            if b in backtofront:
                if seen and seen[-1] == backtofront[b]:
                    seen.pop()
                else:
                    return False

            else:
                seen.append(b)
        return True if not seen else False