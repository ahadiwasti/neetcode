class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = len(nums1)-1
        num1pointer = m-1
        num2pointer = n-1

        while num2pointer >= 0:
            if num1pointer >= 0 and nums1[num1pointer] > nums2[num2pointer]:
                nums1[last] = nums1[num1pointer]
                num1pointer-=1

            else:
                nums1[last] = nums2[num2pointer]
                num2pointer-=1
            
            last-=1
        print(nums1)