class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]*len(nums)
        for j in range(len(nums)-2,-1,-1):            
            res[j] = res[j+1]*nums[j+1]
        dup = nums[0]
        for i in range(1,len(nums)):
            res[i] = res[i]*dup
            dup*=nums[i]
        return res
        
