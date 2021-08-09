def trap(self, height: List[int]) -> int:
        leftmax = [0]*len(height)
        rightmax = [0]*len(height)
        S = 0
        m = 0
        for i in range(len(height)):
            m = max(m,height[i])
            leftmax[i] = m
        m = 0    
        for j in range(1,len(height)+1):
            m = max(m,height[-j])
            rightmax[-j] = m
        for i in range(len(height)):
            S += min(leftmax[i],rightmax[i]) - height[i]
        return S    
