class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tem = list(set(nums))
        tem.sort()
        nums[:len(tem)] = tem
        return len(tem)
