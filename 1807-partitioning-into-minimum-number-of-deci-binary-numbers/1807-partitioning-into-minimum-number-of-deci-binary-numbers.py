class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        count=0
        num=int(n)
        while num!=0:
           reduceStr = ''.join('1' if dig != '0' else '0' for dig in str(num))
           num = num-int(reduceStr)
           count+=1
        return count
            
