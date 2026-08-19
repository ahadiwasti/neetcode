class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insertpoint = len(nums1)-1
        num1len = m-1
        num2len = n-1

        while num2len >=0:
            if num1len >= 0 and nums1[num1len] > nums2[num2len]:
                nums1[insertpoint] = nums1[num1len]
                num1len-=1
            else:
                nums1[insertpoint] = nums2[num2len]
                num2len-=1

            insertpoint-=1
                
