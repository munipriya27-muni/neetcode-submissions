class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicia = {}
        dicib = {}
        for i in s:
            if i in dicia:
                dicia[i] += 1
            else:
                dicia[i] = 1
        
        for i in t:
            if i in dicib:
                dicib[i] += 1
            else:
                dicib[i] = 1
        
        if dicia == dicib:
            return True
        return False