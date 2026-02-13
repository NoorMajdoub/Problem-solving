class Solution(object):
    def restoreString(self, s, indices):
                res=[0]*len(s)
                for i ,idd in enumerate(indices):
                   # print(i,idd)
                    res[idd]=s[i]
                return ''.join(res)
                
