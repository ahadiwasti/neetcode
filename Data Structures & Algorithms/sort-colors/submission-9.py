class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = defaultdict(int)

        for num in nums:
            freq[num]+=1
        idx = 0
        maxval = max(nums)
        for i in range(maxval+1):
            while freq[i]:
                nums[idx] = i
                idx+=1
                freq[i]-=1

        return nums