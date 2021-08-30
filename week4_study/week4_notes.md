DFS & BFS search: These modules can be applied to all the data structure but they are largely in use with graph / tree search 


modules: 
## Recursion Methods: 
```
visited = set() 

def dfs(node,visited):
    if node in visited: 
       return 
       
    #add the node in the visited set 
    visited.add(node) 
    
    #process the current node here: 
    #它并没有在loop 完成的时候就已经走到下一层了
    for next_node in node.children(): 		
        #if the node is not in the visited node, then it should not be visited 
        if next_node not in visited: 			
           dfs(next_node, visited)
```
## Non-recursion methods: 
```
def DFS(self,tree):
    
    if tree.root is None: 
       return [] 
       
    #initize the visited and with a stack 
    visited,stack = [], [tree.root]
    
    #while the stack is not null 
    while stack: 
        #pop the stack (LIFO) 
        node = stack.pop() 
        #if they are in the tree, and it should be added 
        visited.add(node)
        
        #need to process the node 
        process(node) 
        
        nodes = generate_related_nodes(node)
        stack.push(nodes)
              
```
    
    
## Tree Modules Definition: 
* Everynode should be traversed 
* Every node shoud lbe visited only once 
* DFS/ BFS / Prim/ Dijkrstra 

The tree: DFS 
```
def dfs(node):
    
    if node in visited: 
        return 
        
    visited.add(node) 
    
    #visit the left children and the right children 
    dfs(node.right)
    dfss(node.left) 
```

The Graph: DFS
Example: Non-directed Graph: 


```
#queue to represent the BFS 
def BFS(graph,start,end): 
    visited = set() 
    
    queue = [] 
    queue.append(start) 
    
    while queue: 
        node = queue.pop() 
        visited.node(add) 
        
    
    process(node)
    nodes = generate_related_nodes(node)
    queue.push(nodes) 
```

Greedy Algos: 
1. Choose the best in every step in order to achieve global optimal 
* The difference between Greedy and Dynamic Programming: 
* The greedy algorithm could not be backtracked while the dynamic programming needs backtracked (may be global optimal) ? 
* Greedy: Optimization on minimum spanning tree , Hoffman code (Xgboost needs not the global optimal algos but it is very fast) 

Example:
https://leetcode-cn.com/problems/coin-change/ 


Binary Search: 
1. monotonicity 
2. bounded 
3. index accessible 

```
# Python

left, right = 0, len(array) - 1 
  
while left <= right: 	  
    mid = (left + right) / 2 	  
    if array[mid] == target: 		    
    # find the target!! 		    
    break or return result 	  
    elif array[mid] < target: 		    
    left = mid + 1 	  
    else: 		    
    right = mid - 1
```






