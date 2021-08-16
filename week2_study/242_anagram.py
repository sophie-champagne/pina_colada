class Solution(object):
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #check the length of two string whether they are the same 
        if len(s) <> len(t): return False 
        
        #convert the list to character array 
        s_l = list(s)
        t_l = list(t)
        
        #sort the list 
        s_l.sort()
        t_l.sort()
        
        #unpack two lists and compare one by one 
        for i, j in zip(s_l,t_l): 
            if i == j: 
                pass 
            else:
                return False 
        
        return True 
      
#construct a dictionary(hash) and count the frequencies 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        #compare the length 
        if len(s) <> len(t): return False 
        #construct a dictionary in python 
        stas = {}
        stat = {}
        
        #count the ch value in the stats 
        for ch in s:
            stas[ch] = stas.get(ch,0)+1
        for ch in t:
            stat[ch] = stat.get(ch,0) + 1
            
        if stas == stat:
            return True
        else:
            return False
          

