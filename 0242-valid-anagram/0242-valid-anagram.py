class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d={}
        if len(s)!=len(t): return False
        for c in s:
            d[c] = 1 if not d.get(c) else d[c]+1
        for c in t:
            if not d.get(c) or d[c]==0: return False
            d[c]-=1
        return True
