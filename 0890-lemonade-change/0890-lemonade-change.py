class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = ten = 0
        for b in bills:
            if b==5: five+=1
            elif b==10:
                if five: five-=1; ten+=1
                else: return False
            else:
                if ten and five: five-=1; ten-=1
                elif five>=3: five-=3
                else: return False
        return True
        