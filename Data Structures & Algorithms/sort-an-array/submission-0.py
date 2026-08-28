class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        minval,maxval = min(nums),max(nums)

        for num in nums:
            count[num]+=1
        index = 0
        for val in range(minval,maxval+1):
            while count[val]:
                nums[index] = val
                index +=1
                count[val] -=1

        return nums

        