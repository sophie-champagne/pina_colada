#brute force: 
#time complexity: O(n^2) 
#example: [2,7,11,15] 9 
# 2 

#range function: range(start,stop,step) , [), left inclusive and right exlusive for python 
#range(5), 0,1,2,3,4

#the first input: array 
# i = 2 
# the j would loop through [1,2,3,4]
# if they found something matching the target , just output 

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                  
#hashmap solution: python dict is using hashmap/hashtable 
#It supports the lookup table to the constant time
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        #write in a hashmap 
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        #loop through the nums and get the hashmap function 
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            
            if j is not None and i!= j:
                return [i,j]
              
