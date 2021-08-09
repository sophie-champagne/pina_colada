class Solution:
    def rotate(self, nums, k):
        retote = []
        k = k % len(nums)
        retote = nums[:len(nums)-k]
        for i in range(len(nums)-k):
            del nums[0]
        nums.extend(retote)

