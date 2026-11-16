class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for id,num in enumerate(numbers):
            if target-num in seen:
                return [seen[target-num]+1, id+1]

            else:
                seen[num] = id

        return []