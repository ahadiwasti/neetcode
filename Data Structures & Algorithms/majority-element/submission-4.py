class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pointer = 0
        counter = 0

        for num in nums:
            if counter == 0:
                pointer = num
            
            counter += (1 if pointer == num else -1)

        return pointer