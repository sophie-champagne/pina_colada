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
![image info](https://leetcode.com/problems/fibonacci-number/Figures/509/fibonacciRecursion5.png)



































