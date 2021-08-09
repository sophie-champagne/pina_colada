class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        left = 0
        right = m
        while left <= right < m + n:
            if nums1[left] > nums1[right]:
                tmp = nums1[right]
                nums1[left + 1:right + 1] = nums1[left:right]
                nums1[left] = tmp
                left += 1
                right += 1
            else:
                left += 1
