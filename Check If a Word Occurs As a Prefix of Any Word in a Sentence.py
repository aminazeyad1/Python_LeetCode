import re
class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split()

        for i, word in enumerate(words):
            if re.match("^{}".format(searchWord), word):

                return i+ 1
            
        else:
               return -1
        