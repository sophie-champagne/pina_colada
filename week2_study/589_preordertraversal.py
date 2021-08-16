"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        #保存节点值
        result = []
        #pre order traversal 
        def pre_order(root):
            #
            if root:
                #root be in the vale 
                result.append(root.val)
                #recursion 
                for node in root.children:
                    pre_order(node)
        pre_order(root)
        return result

