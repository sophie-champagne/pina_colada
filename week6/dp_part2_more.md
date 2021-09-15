https://leetcode.com/problems/triangle/description/

## The first thought: 
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3

I think the brute-force method applies here from my first intuition: (they have restrcition that they can not jump by level) 
(1) Recursive method for going either left or right 
(2) List all the combination of the results 

DP: 
(1) Repeat structure,subproblem: 
I am thinking that the min between the second layer 3 or 4, which would be the smaller of the two. 
Say, f[i,j] = min{sub[i+1],j], sub[i+1,j+1]} 

The i+1 means the +1 layer and j+1 means elements in the same layer 

(2) Define the State 
If it is already had the f[i,j] transition state, then we can write the formula like this
f[i,j] = f[i+1,j] + f[i+1,j+1] + a[i,j]
(3) DP formula 
(bottom-up or top-down) 

Brute Force Method: 


The DP method: 

https://leetcode.com/problems/maximum-subarray/

https://leetcode.com/problems/house-robber/




