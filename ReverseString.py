
class Solution(object):
    def reverseString(self, s):
        s[:]= list(reversed(str(''.join(["h","e","l","l","o"]))))
#or do
class Solution(object):
    def reverseString(self, s):
            s[:]= s[::-1]
