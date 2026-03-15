class Solution(object):
    def findContentChildren(self, g, s):
        i=0
        j=0
        happy=0
        g=sorted(g)
        s=sorted(s)
        while i < len(g) and j < len(s):
            if s[j] >=g[i]:
                happy+=1
                
                i+=1
            j+=1
        return happy
        
