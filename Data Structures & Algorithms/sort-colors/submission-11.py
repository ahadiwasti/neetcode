class Solution:
    def sortColors(self, nums)->list:
        freq = defaultdict(int)

        for num in nums:
            freq[num]+=1

        index = 0

        for i in range(3):
            while freq[i]:
                nums[index] = i
                index+=1
                freq[i]-=1

        return nums