class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        s = ""
        ind = 0
        for (c1,c2) in zip(word1,word2):
            s+=c1+c2
            ind += 1
        s+=word1[ind:]+word2[ind:]
        return s

        