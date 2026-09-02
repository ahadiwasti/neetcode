class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        freq = defaultdict(int)
        res = []
        for num in nums:
            freq[num]+=1

        minval,maxval = min(nums),max(nums)
        index=0
        for i in range(minval,maxval+1):
            while freq[i]:
                nums[index] = i
                freq[i] -=1
                index+=1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1

            while l < r:
                threesum = nums[l]+nums[r]+nums[i]
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1

                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1

                    while l < r and nums[l] == nums[l-1]:
                        l+=1

        return res

# T:O(n'2)
# S:O(n)
