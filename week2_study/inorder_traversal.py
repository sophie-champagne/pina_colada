class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
    #initialize a result set 
		res = []
    
    #if the root is null then return null 
		def dfs(root):
			if not root:
				return

     #apply recursive method and define the print left, value and right 
			dfs(root.left)
			res.append(root.val)
			dfs(root.right)
		
    dfs(root)
		return res

