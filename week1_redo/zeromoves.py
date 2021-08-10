#zeromoves: https://mp.weixin.qq.com/s/_p7grwjISfMh0U65uOyCjA 

#remove the elements 

##better solution 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      
        if not nums: 
            return 0 
        
        j = 0 
        for i in range(len(nums)):
            if nums[i]: 
                nums[j],nums[i] = nums[i],nums[j]
                j+=1
                
 
 ##first solutions 
 class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      
        if not nums: 
            return 0 
        
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j+=1
        
        for i in range(j,len(nums)):
            nums[i] = 0 
        
        return nums
      
    
