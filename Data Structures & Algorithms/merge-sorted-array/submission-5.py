class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insertpoint = len(nums1)-1
        num1 = m-1
        num2 = n-1

        while num2 >= 0:
            if num1>=0 and nums1[num1]>nums2[num2]:
                nums1[insertpoint] = nums1[num1]
                num1-=1
            else:
                nums1[insertpoint] = nums2[num2]
                num2-=1
            insertpoint-=1
            

