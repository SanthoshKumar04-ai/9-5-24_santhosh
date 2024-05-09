class Solution(object):
    def isValid(self, s):
        for i in range(len(s)):
            s = s.replace('{}', '').replace('[]', '').replace('()', '')
        return s == ''
