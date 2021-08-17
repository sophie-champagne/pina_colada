class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        #deque the stack 
        value, s = [], []
        q = deque()
        d = 1
        if root:
            q.append(root)
        while q:
            cur = q.popleft()
            s.append(cur.val)
            for child in cur.children:
                q.append(child)
            d -= 1
            if d == 0:
                value.append(s)
                d = len(q)
                s = []
        return value

