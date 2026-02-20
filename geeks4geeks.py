#Check Equal Arrays
class Solution:
    def checkEqual(self, a, b) -> bool:
       return sorted(a)==sorted(b)
#Union of Arrays with Duplicates
class Solution:    
    def findUnion(self, a, b):
        return list(set(a+b))
#Array Subset

from collections import Counter
class Solution:
    def isSubset(self, a, b):
       return Counter(b) <= Counter(a)
    
    
    
    
