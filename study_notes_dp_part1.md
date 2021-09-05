The visaulization of the dp 

https://visualgo.net/en

```
# Python

def recursion(level, param1, param2, ...):     
    # recursion terminator     
    if level > MAX_LEVEL: 	   
        process_result 	   
        return     
    
    # process logic in current level     
     process(level, data...)     
    # drill down     
      self.recursion(level + 1, p1, ...)     
         
    # reverse the current level status if needed

```

```
# Python

def divide_conquer(problem, param1, param2, ...):   
    # recursion terminator   
    if problem is None: 	
       print_result 	
       return   
    
    # prepare data   
    data = prepare_data(problem)   
    subproblems = split_problem(problem, data)   
    
    # conquer subproblems   
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)   
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)   
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)   …  
    
    # process and generate the final result   
    result = process_result(subresult1, subresult2, subresult3, …)	  
    
    
    # revert the current level states

```
* In both contexts it refers to simplifying a complicated problem by breaking it down into simpler sub-problems in a recursive manner. 
While some decision problems cannot be taken apart this way, decisions that span several points in time do often break apart recursively. 


* divide and conquer: a special version of recursion 
* backtracking 
* recursiong 
* dynamic programming: divide and conquer + optimal substrcuture, if you do not have optimal substruture, you have to loop through everything. 

Complexity: 
from 2 to n to n squared 

The simple Fibonacci sequence: 

The traditional solution for recursion: 
```
class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0: 
            return 0
        if n == 1:
            return 1
        #the recursive part 
        return self.fib(n-1)+self.fib(n-2)

```

The complexity of this method: 
Since we are building trees on a recursive level, then when we get another level, it is 2 to power of n. 
![image info](https://leetcode.com/problems/fibonacci-number/Figures/509/fibonacciRecursion5.png)

Second Method: Using memorization to memorize the previous output then store them in a temp result set. This could be done with an array or list. 
From the above graph, we know that there are so many mid-calculations that we can replicate. Like if we are going to calculate the Fib(6), we can reuse the fib(4) again and again. 

The complexity of this is from O(2 to the power of n) to O(n) 

```
class Solution:
    #initialize a dict in python 
    cache = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        #this line of code just to check the temp result is existed and they can be n 
        if n in self.cache:
            return self.cache[n]
        
        #using the cache[n] to calculate the fib(n-1) and fib(n-2) 
        self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        #return the final cache result 
        return self.cache[n]

```
The 3rd method is the bottom-up method: 
This would be using loops to create elements from n to n - 2 
Most of the competitive DP programming is inclined to use the bottom-up approach as an idea approach for the most of the DP problems 

```
class Solution:
    def fib(self, N: int) -> int:
        #the termination conditions 
        if (N <= 1):
            return N
        
        #set the initialization condition 
        current = 0
        prev1 = 1
        prev2 = 0

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current
```

The second classic kind of DP problems: counting the paths, (fibonacci is the like the first dimension of the DP problem and the path counting is like the seond dimension of DP problem). 

The person can only walk to the right and walk down the path: https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/

https://leetcode.com/problems/unique-paths/
https://leetcode-cn.com/problems/unique-paths-ii/

## Key points about DP: 
1. The optimal substructure : optimal[n] = best_of(optmial[n-1],optimal[n-2])
2. intermediate storage: opt[i]
3. State Transition formula 
opt[i,j] = opt[i+1][j] + opt[i][j+1]


## Other example: The Longest Common Sequence : 
This is the another special case about DP for the string type of problems 

https://leetcode.com/problems/longest-common-subsequence/
Introduction Video: https://www.youtube.com/watch?v=V5hZoJ6uK-s

First thoughts about the solution: 
1. Generate all the combination of the text combination as many as possible 
2. Then check whether certain strings are in these combination 

This question boils down to calcuate the edit distance between the two strings: 

```
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    
        m, n = len(text1), len(text2)
        #initalize the two dimension matrix 
        f = [[0] * (n + 1) for _ in range(m + 1)]
        
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                #from the last element 
                if text1[i - 1] == text2[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])
        
        return f[m][n]
```

Top-down method: Recursion + Memorization 
Bottom-up method: Formula 

DP solver general rules: 
1. 打破思维惯性
2. 理解复杂逻辑关键
3. 职业进阶要领  

1. Define Subproblems 
2. Guess (part of the solution) 
3. relate sub-problem solutions 
4. recursive or memorize (or build the DP table bottom-up) 
5. Solve original problem 

































