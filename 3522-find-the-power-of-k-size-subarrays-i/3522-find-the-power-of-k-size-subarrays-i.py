class Solution(object):    
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res=[]
        count=1
        if len(nums)==1 or k==1: return nums
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count+=1
            else: count=1
            if i>=k-1:
                if count==k:
                    res.append(nums[i])
                    count-=1
                else:
                     res.append(-1)
        return res