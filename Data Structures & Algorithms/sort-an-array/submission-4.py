class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minval,maxval = min(nums), max(nums)
        index = 0
        freq = defaultdict(int)
        for num in nums:
            freq[num] +=1

        for i in range(minval, maxval+1):
            while freq[i]:
                nums[index] = i
                freq[i]-=1
                index +=1

        return nums