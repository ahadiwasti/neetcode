class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minval,maxval = min(nums), max(nums)
        freq = defaultdict(int)
        idx = 0

        for num in nums:
            freq[num] +=1

        for i in range(minval,maxval+1):
            while freq[i]:
                nums[idx] = i
                idx +=1
                freq[i]-=1
        return nums
