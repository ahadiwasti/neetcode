class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0]*3
        for num in nums:
            freq[num]+=1

        index = 0
        for i in range(3):
            while freq[i]:
                nums[index] = i
                index+=1
                freq[i]-=1

        

# T:O(n)
# S:O(1)
        