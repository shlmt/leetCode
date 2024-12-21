class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ht = {}
        oper = 0
        for n in nums:
            val = ht.get(k-n,0)
            if val != 0:
                ht[k-n] = val-1
                oper+=1
            else:
                ht[n] = ht.get(n,0)+1
        return oper