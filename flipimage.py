class Solution(object):
    def flipAndInvertImage(self, arr):
                def aswipe(a):
                        return [0 if el ==1 else 1 for el in a]
                arr=[aswipe(a[::-1]) for a in arr]
                return arr
