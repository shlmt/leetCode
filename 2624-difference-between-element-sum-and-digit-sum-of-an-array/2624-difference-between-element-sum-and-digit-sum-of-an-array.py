class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count1=count2=0
        for x in nums:
            count1+=x
        for y in nums:
            while(y!=0):
                count2+=y%10
                y/=10

        return abs(count2-count1)