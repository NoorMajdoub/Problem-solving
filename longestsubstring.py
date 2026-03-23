class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i=0
      
        res=0
        elems=set()
        for j in range(len(s)):
            while s[j] in elems:
                elems.remove(s[i])
                i+=1
            elems.add(s[j])
            res=max(res,j-i+1)
        return res
