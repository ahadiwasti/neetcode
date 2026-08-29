class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minval,maxval = min(nums),max(nums)
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1

        index = 0
        for i in range(minval,maxval+1):
            while freq[i]:
                nums[index] = i
                index+=1
                freq[i]-=1

        return nums
